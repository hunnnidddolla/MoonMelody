import flet as ft
import colors as c
from flet import alignment
class CustomInputfield(ft.UserControl):
    def __init__(self,title: str):
        super().__init__()
        self.input = ft.TextField(
            height=50,
            border_color=c.pink17,
            border_width=1.5,
            cursor_height=20,
            cursor_width=2,
            cursor_color=c.pink13,
            color=c.pink17,
            text_size=20,
            bgcolor='transparent',
            on_focus=self.focus_shadow,
            on_blur=self.blur_shadow,
            on_change=self.set_loader_animation
        )
        self.input_box = ft.Container(
            expand=True,
            content=self.input,
            width=1000,

            animate=ft.Animation(300, 'ease'),

        )
        self.loader = ft.ProgressBar(
            value=0,
            bar_height=1.5,
            color=c.pink17,
            bgcolor='transparent',
        )

        self.object = self.create_input(title)


    def focus_shadow(self, e):
        self.input.border_color = c.w
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=1,
            color=ft.colors.with_opacity(0.25, 'black'),
            offset=ft.Offset(4, 4)
        )
        self.update()
        self.set_loader_animation(None)

    def blur_shadow(self, e):
        self.input_box.shadow = None
        self.input.border_color = c.pink17
        self.update()
        self.set_loader_animation(None)

    def set_loader_animation(self, e):
        if len(self.input.value)!=0:
            self.loader.value = None
        else:
            self.loader.value=0
        self.loader.update()
        self.update()

    def create_input(self, title):

        return ft.Column(
            spacing=5,
            alignment=alignment.center,
            controls=[
                ft.Text(title, size=22, weight='bold', color=c.pink17),
                ft.Stack(
                    [self.input_box],
                    alignment=ft.alignment.top_right,),

                    self.loader
            ],
        )

    def build(self):
        return self.object


