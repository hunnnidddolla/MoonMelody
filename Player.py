from flet import *
import colors as c
from CustomInputfield import CustomInputfield
import asyncio

class Player(UserControl):
    def __init__(self, page: Page, res: str):
        super().__init__()
        self.page = page
        self.audio1 = Audio(src=res,autoplay=False,
        volume=1,balance=0,on_loaded=self.on_audio_loaded,
        on_duration_changed=self.on_duration_changed,
        on_position_changed=self.on_position_changed,
        on_state_changed=lambda e: print("State changed:", e.data),
        on_seek_complete=lambda _: print("Seek complete"),)
        self.progress_slider = Slider(
        min=0, max=100, thumb_color=c.pink17, inactive_color='surface,0.01',
        active_color=c.pink17, width=1000, on_change=self.on_slider_change)

    def on_audio_loaded(self, e):
        self.page.update()
    def on_duration_changed(self, e):
        self.progress_slider.max = e.data
        self.progress_slider.update()
    def on_position_changed(self, e):
        if not getattr(self, 'slider_is_dragging', False):
            self.progress_slider.value = e.data
            self.progress_slider.update()
    def on_slider_change(self, e):
        self.slider_is_dragging = True
        self.audio1.seek(position_milliseconds=int(e.control.value))
        self.slider_is_dragging = False
    def set_volume(self, e):
        new_volume = e.control.value / 100
        self.audio1.volume = new_volume
        self.audio1.update()
        print(f"Volume set to {new_volume}")
    def mute(self, e):
        e.control.icon = icons.VOLUME_MUTE_ROUNDED
        e.control.update()
        if self.audio1.volume:
            print(e.control.content)
            self.audio1.volume = 0.0
            self.audio1.update()
        else:
            e.control.icon = icons.VOLUME_DOWN_ROUNDED
            e.control.update()
            self.audio1.volume = 1.0
            self.audio1.update()
    def play_audio(self, e):
        if self.audio1 not in self.page.overlay:
            self.page.overlay.append(self.audio1)
        self.page.update()
        self.audio1.play()
        self.page.update()
    def build(self):
        return Container(width=900,height=500,
        bgcolor='transparent',content=Column(controls=[
        Column(controls=[Row(controls=[
        Rive(src='Animation/new_file (14).riv', width=150, height=150, scale=1)]
        , alignment='center'),Text('   Result', size=18, color=c.pink17),
        self.progress_slider],width=1000),Row(controls=[
        IconButton(icon=icons.FAVORITE_ROUNDED, icon_color=c.pink17, icon_size=30),
        IconButton(icon=icons.VOLUME_DOWN_ROUNDED, on_click=self.mute, icon_color=c.pink17, icon_size=30),
        Slider(min=0, max=100, value=self.audio1.volume * 100, thumb_color=c.pink17, on_change=self.set_volume,
        active_color=c.pink17, inactive_color='surface,0.01', width=100),
        IconButton(icon=icons.PLAY_ARROW, on_click=self.play_audio, icon_color=c.pink17, icon_size=30,
        alignment=alignment.center),
        IconButton(icon=icons.PAUSE_CIRCLE_SHARP, on_click=lambda _: self.audio1.pause(),
        icon_color=c.pink17,
        icon_size=30, alignment=alignment.center),],alignment='center',spacing=10,width=1000,height=40)]))

