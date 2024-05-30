from flet import *
from CustomInputfield import CustomInputfield
from GenerationFunc import generate_music
import colors as c
from Player import Player
import asyncio
import tempfile
import os
from db import supabase
class PageGenerate(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.input = CustomInputfield('TEXT PROMPT')
        self.duration=29
        self.model_type='medium'
        self.player = None
        self.generated_track = None
        self.controls = []
        self.drop_model = Dropdown(label="Model Type",label_style=TextStyle(color=c.pink17,size=18),
            bgcolor='transparent',border_color=c.pink17,border_width=0.6,color=c.pink17,text_size=18,
            focused_color=colors.with_opacity(0.7,c.pink17),
            options=[
                dropdown.Option("small", "Small"),
                dropdown.Option("medium", "Medium"),
                dropdown.Option("large", "Large")
            ],
            value="medium",
            on_change=self.on_model_change
        )
        self.duration_slider= Slider(
                label="Duration (seconds)",
                min=10,
                max=300,
                divisions=29,
                value=self.duration,
                on_change=self.on_duration_change,
                active_color=c.pink17,
                inactive_color='surface,0.01'
            )

    def on_duration_change(self, e):
        self.duration = int(e.control.value)

    async def generate_to_user_prompt(self, e):
        user_id = self.page.client_storage.get('current_user')
        prompt = self.input.input.value
        title = prompt.split()[0]
        self.title = f'{title}.wav'
        await self.clear_player()
        user_id=self.page.client_storage.get('current_user')
        await generate_music(prompt, self.title,user_id,self.model_type,self.duration)
        self.generated_track = f"src/{self.title}"
        await self.initialize_player()

    async def clear_player(self):
        self.generated_track = None
        if self.player and self.player in self.page.overlay:
            self.page.overlay.remove(self.player)
        self.player = None
        self.controls.clear()
        self.controls.extend([Container(padding=padding.only(left=40, top=20), content=Column(controls=[
        self.input,self.drop_model,self.duration_slider,ElevatedButton(
        content=Row([Icon(name=icons.WAVES_SHARP, color=c.pink17, size=18),
        Text(value='Generate', size=18, color=c.pink17)], alignment='center'),width=200,height=50,
        on_click=lambda e: self.generate_to_user_prompt_sync(e),bgcolor=colors.with_opacity(0.45, c.pink17),
        on_hover=lambda e: self.Highlight(e),),Divider(height=5, color='transparent'),
        Column(controls=[self.player.build() if self.player else Row(controls=[
        Rive(src='Animation/new_file (11).riv', width=150, height=150, scale=1)], alignment='center')],
        width=900,height=500,horizontal_alignment=alignment.bottom_center,expand=True),]))])
        self.update()

    def on_model_change(self, e):
        self.model_type = e.control.value
    async def initialize_player(self):
        if self.generated_track:
            self.player = Player(self.page, self.generated_track)
            self.page.update()
            await self.update_content()

    async def update_content(self):
        self.controls.clear()
        self.controls.extend([Container(padding=padding.only(left=40, top=20),content=Column(controls=[
            self.input,
            self.drop_model,
            self.duration_slider,
            ElevatedButton(
                content=Row([
                    Icon(name=icons.WAVES_SHARP, color=c.pink17, size=18),
                    Text(value='Generate', size=18, color=c.pink17)
                ], alignment='center'),
                width=200,
                height=50,
                on_click=lambda e: self.generate_to_user_prompt_sync(e),
                bgcolor=colors.with_opacity(0.45, c.pink17),
                on_hover=lambda e: self.Highlight(e),
            ),
            Divider(height=5, color='transparent'),
            Column(
                controls=[
                    self.player.build() if self.player else Row(controls=[
                        Rive(src='Animation/new_file (11).riv', width=150, height=150, scale=1)],alignment='center')
                ],
                width=900,
                height=500,
                horizontal_alignment=alignment.bottom_center,
                expand=True
            ),
        ]))])
        self.update()

    def Highlight(self, e):
        if e.data == 'true':
            e.control.border_color = c.pink17
            e.control.shadow = BoxShadow(
                spread_radius=6,
                blur_radius=8,
                color=colors.with_opacity(0.15, 'black'),
                offset=Offset(4, 4)
            )
            e.control.bgcolor = colors.with_opacity(0.8, c.pink17)
            e.control.update()
            e.control.content.controls[0].color = 'white54'
            e.control.content.controls[1].color = 'white54'
            e.control.content.update()
        else:
            e.control.bgcolor = colors.with_opacity(0.45, c.pink17)
            e.control.update()
            e.control.content.controls[0].color = c.pink17
            e.control.content.controls[1].color = c.pink17
            e.control.content.update()

    def build(self):
        return Container(padding=padding.only(left=100, top=20),
            content=Column(controls=[self.input,self.drop_model,self.duration_slider,
                    ElevatedButton(content=Row([Icon(name=icons.WAVES_SHARP, color=c.pink17, size=18),
                            Text(value='Generate', size=18, color=c.pink17)], alignment='center'),
                        width=200,height=50,on_click=lambda e: self.generate_to_user_prompt_sync(e),
                        bgcolor=colors.with_opacity(0.45, c.pink17),
                        on_hover=lambda e: self.Highlight(e),),
                    Divider(height=5, color='transparent'),
                    Column(
                        controls=[
                            self.player.build() if self.player else Row(controls=[
                                Rive(src='Animation/new_file (11).riv', width=150, height=150, scale=1)],alignment='center')],
                        width=900,height=500,horizontal_alignment=alignment.bottom_center,
                        expand=True),]))

    def generate_to_user_prompt_sync(self, e):
        asyncio.run(self.generate_to_user_prompt(e))

