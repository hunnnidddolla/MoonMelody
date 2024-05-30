from flet import *
from sidebar import ModernNavBar
from UserData import UserData
import time


class CustomPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    def AnimatedNavBar(self, e):
        if self.controls[0].width != 50:
            for item in self.controls[0].content.controls[0].content.controls[0].content.controls[1].controls:
                item.opacity = 0
                item.update()
            for items in self.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(item, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()
            time.sleep(0.2)
            self.controls[0].width = 50
            self.controls[0].update()
        else:
            self.controls[0].width = 200
            self.controls[0].update()
            time.sleep(0.2)
            for item in self.controls[0].content.controls[0].content.controls[0].content.controls[1].controls:
                item.opacity = 1
                item.update()
            for items in self.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(item, Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()
    def build(self):
        return Container(
            width=200,
            height=650,
            border_radius=10,
            padding=padding.only(right=10),
            alignment=alignment.top_left,
            animate=animation.Animation(500, 'decelerate'),
            bgcolor='transparent',
            content=ModernNavBar(
                func=self.AnimatedNavBar,
                user=UserData('MM', 'Moon Melody', 'User'),
            )
        )




