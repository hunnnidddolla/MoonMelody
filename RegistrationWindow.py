import flet as ft
import asyncio
from supabase import Client
from db import supabase
from flet import View, Page, AppBar, ElevatedButton, Text, RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import colors
import logging
import webbrowser
import tempfile
import os
import colors as c

colors_d = dict(pink10='#FFAACC',#Розовая гвоздика
pink11='#DE5D83',#Румянец
pink12='#FFBCD9',#Сладкая вата
pink13='#C08081',#Старинный розовый
pink14='#B57281', #Турецкий розовый
white1='#F5FFFA',#мятно-кремовый
white2='#F0FFF0',#медовая роса
white3='#F5F5F5',)#дымчато белый

class CustomInputfield(ft.UserControl):
    def __init__(self, password: bool, title: str, see: bool):
        super().__init__()
        self.input = ft.TextField(
            value='',
            height=45,
            border_color=colors.pink15,
            border_width=0.6,
            cursor_height=20,
            cursor_width=2,
            cursor_color=colors.pink15,
            color=colors.pink16,
            text_size=25,
            bgcolor=colors.pink18,
            password=password,
            can_reveal_password=see,
            on_focus=self.focus_shadow,
            on_blur=self.blur_shadow,
            on_change=self.set_loader_animation
        )
        self.input_box = ft.Container(
            expand=True,
            content=self.input,
            animate=ft.Animation(300, 'ease'),
        )
        self.loader = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color=colors.pink13,
            bgcolor='transparent',
        )
        self.status = ft.Checkbox(
            value=False,
            disabled=True,
            opacity=0,
            shape=ft.CircleBorder(),
            right=10,
            check_color=colors.pink13,
            animate_opacity=ft.Animation(200, 'linear'),
            animate_offset=ft.Animation(350, 'ease'),
        )
        self.object = self.create_input(title)

    async def set_ok(self):
        self.loader.value = 0
        self.loader.update()
        self.status.opacity = 1
        self.update()
        await asyncio.sleep(1)
        self.status.value = True
        self.status.update()
        self.update()

    def focus_shadow(self, e):
        self.input.border_color = colors.pink13
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, 'black'),
            offset=ft.Offset(4, 4)
        )
        self.update()
        self.set_loader_animation(None)

    def blur_shadow(self, e):
        self.input_box.shadow = None
        self.input.border_color = 'white24'
        self.update()
        self.set_loader_animation(None)

    def set_loader_animation(self, e):
        if len(self.input.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0
        self.loader.update()
        self.update()

    def create_input(self, title):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=18, weight='bold', color=colors.pink13),
                ft.Stack(
                    [self.input_box, self.status],
                    alignment=ft.alignment.top_right,
                ),
                self.loader
            ],
        )

    def build(self):
        return self.object

class MainFromUI(ft.UserControl):
    def __init__(self, supabase_user: Client):
        super().__init__()
        self.supabase_user = supabase_user
        self.email = CustomInputfield(False, 'Email', False)
        self.password = CustomInputfield(True, 'Password', True)
        self.submit = ft.ElevatedButton(width=400,height=45,
        content=ft.Row([ft.Icon(name=ft.icons.KEY, color=colors.pink16),
        ft.Text(value='Submit', size=18, color=colors.pink16)]),bgcolor=colors.pink17,
        on_click=lambda e: asyncio.run(self.log_in_user(e)),
        on_hover=lambda e: self.Highlight(e),)
        self.register = ft.ElevatedButton(width=400,height=45,
        content=ft.Row([ft.Icon(name=ft.icons.STAR, color=colors.pink16),
        ft.Text(value='Sign up', size=18, color=colors.pink16)]),
        bgcolor=colors.pink17,on_click=lambda e: e.page.go('/register'),
        on_hover=lambda e: self.Highlight(e),)


    def Highlight(self, e):
        if e.data == 'true':
            e.control.border_color = colors.pink15,
            e.control.shadow = ft.BoxShadow(
                spread_radius=6,
                blur_radius=8,
                color=ft.colors.with_opacity(0.25, 'black'),
                offset=ft.Offset(4, 4)
            )
            e.control.bgcolor = colors.pink17
            e.control.update()
            e.control.content.controls[0].icon_color = colors.pink13
            e.control.content.controls[1].color = colors.pink13
            e.control.content.update()
        else:
            e.control.bgcolor = colors.pink17
            e.control.update()
            e.control.content.controls[0].icon_color = colors.pink16
            e.control.content.controls[1].color = colors.pink16
            e.control.content.update()

    async def log_in_user(self, event):
        try:
            if self.email.input.value != '' and self.password.input.value != '':
                response=self.supabase_user.auth.sign_in_with_password(
                    {
                        'email': self.email.input.value,
                        'password': self.password.input.value
                    }
                )
                event.page.client_storage.set('current_user', response.user.id)
                await asyncio.sleep(0.5)
                await self.email.set_ok()
                await asyncio.sleep(0.5)
                await self.password.set_ok()
                self.submit.bgcolor = 'white24'
                self.update()
                event.page.go("/home")
        except Exception as e:
            logging.error(f"Error logging in: {e}")
            await self.show_error_message(event.page, str(e))



    async def show_error_message(self, page, message):

        error_dialog = ft.AlertDialog(
            bgcolor='transparent',
            title=ft.Text("Error",color=c.pink17,size=30),
            content=ft.Text('Login Error',color=c.pink17,size=20),
            actions=[
                ft.ElevatedButton(
                    bgcolor='transparent',
                    content=ft.Text("Close",color=c.pink17,size=20),
                    on_click=lambda e: close(e)
                )
            ]
        )
        def close(e):
            error_dialog.open=False
            self.page.update()
        page.dialog = error_dialog
        page.dialog.open = True
        await page.update_async()

    def build(self):
        return ft.Container(width=450,height=550,
        alignment=ft.alignment.center,bgcolor=ft.colors.with_opacity(0.1, colors.pink13),
        border_radius=10,padding=20,
        content=ft.Column(horizontal_alignment='center',alignment='center',
        controls=[ft.Text('Sign in', size=30, weight='w800', color=colors.pink13),
        ft.Divider(height=25, color='transparent'),self.email,self.password,
        ft.Divider(height=5, color='transparent'),self.submit,
        ft.Divider(height=5, color='transparent'),self.register,]))

class Register_Window(ft.UserControl):
    def __init__(self, supabase_user: Client):
        super().__init__()
        self.supabase_user = supabase_user
        self.email = CustomInputfield(False, 'Email', False)
        self.password = CustomInputfield(True, 'Password', True)
        self.register = ft.ElevatedButton(width=400,height=45,
        content=ft.Row([ft.Icon(name=ft.icons.KEY, color=colors.pink16),
        ft.Text(value='Submit', size=18, color=colors.pink16)]),
            bgcolor=colors.pink17,
            on_click=lambda e: asyncio.run(self.create_user(e)),
            on_hover=lambda e: self.Highlight(e),)
        self.back = ft.ElevatedButton(width=400,height=45,
        content=ft.Row([ft.Icon(name=ft.icons.KEYBOARD_BACKSPACE, color=colors.pink16),
        ft.Text(value='Back', size=18, color=colors.pink16)]),bgcolor=colors.pink17,
        on_click=lambda e: e.page.go('/auth'),on_hover=lambda e: self.Highlight(e),)

    def Highlight(self, e):
        if e.data == 'true':
            e.control.border_color = colors.pink15,
            e.control.shadow = ft.BoxShadow(
                spread_radius=6,
                blur_radius=8,
                color=ft.colors.with_opacity(0.25, 'black'),
                offset=ft.Offset(4, 4)
            )
            e.control.bgcolor = colors.pink17
            e.control.update()
            e.control.content.controls[0].icon_color = colors.pink13
            e.control.content.controls[1].color = colors.pink13
            e.control.content.update()
        else:
            e.control.bgcolor = colors.pink17
            e.control.update()
            e.control.content.controls[0].icon_color = colors.pink16
            e.control.content.controls[1].color = colors.pink16
            e.control.content.update()

    async def create_user(self, event) -> None:
        if self.email.input.value != '' and self.password.input.value != '':
            try:
                response = self.supabase_user.auth.sign_up(
                    {'email': self.email.input.value,'password': self.password.input.value})
                data = {'email': self.email.input.value,'password': self.password.input.value}
                self.supabase_user.table('users').insert(data).execute()
                event.page.client_storage.set('current_user', response.user.id)
                await asyncio.sleep(0.5)
                await self.email.set_ok()
                await asyncio.sleep(0.5)
                await self.password.set_ok()
                self.register.bgcolor = colors.pink17
                self.email.input.value, self.password.input.value = '', ''
                self.update()
                event.page.go("/home")
            except Exception as e:
                logging.error(f"Error creating user: {e}")
                await self.show_error_message(event.page, str(e))

    async def show_error_message(self, page, message):
        error_dialog = ft.AlertDialog(
            bgcolor='transparent',
            title=ft.Text("Error",color=c.pink17,size=30),
            content=ft.Text('Login Error',color=c.pink17,size=20),
            actions=[
                ft.ElevatedButton(
                    bgcolor='transparent',
                    content=ft.Text("Close",color=c.pink17,size=20),
                    on_click=lambda e: close(e)
                )
            ]
        )
        def close(e):
            error_dialog.open=False
            self.page.update()
        page.dialog = error_dialog
        page.dialog.open = True
        await page.update_async()
    def build(self):
        return ft.Container(width=450,height=600,alignment=ft.alignment.center,
        bgcolor=ft.colors.with_opacity(0.1, colors.pink13),border_radius=10,
        padding=20,content=ft.Column(horizontal_alignment='center',alignment='center',
        controls=[ft.Text('Sign up', size=30, weight='w800', color=colors.pink13),
        ft.Divider(height=25, color='transparent'),self.email,self.password,
        ft.Divider(height=5, color='transparent'),self.register,
        ft.Divider(height=5, color='transparent'),self.back]))


