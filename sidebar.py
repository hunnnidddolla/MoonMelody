from flet import*
import colors as c
from UserData import UserData
from functools import partial
class ModernNavBar(UserControl):
    def __init__(self,func,user:UserData):

        self.func = func
        self.user=user
        super().__init__()
    def Highlight(self,e):
        if e.data=='true':
            e.control.bgcolor=colors.with_opacity(0.45,c.pink17)
            e.control.update()
            e.control.content.controls[0].icon_color='white54'
            e.control.content.controls[1].color = 'white54'
            e.control.content.update()
        else:
            e.control.bgcolor=None
            e.control.update()
            e.control.content.controls[0].icon_color = c.pink17
            e.control.content.controls[1].color = c.pink17
            e.control.content.update()


    def ContainedIcons(self,icon_name:str,text:str,rout):
        return Container(width=180,height=45,
        border_radius=10,on_hover=lambda e:self.Highlight(e),
        on_click=lambda e: e.page.go(f'/{rout}'),content=Row(
        controls=[IconButton(icon=icon_name,icon_size=22,
        icon_color=c.pink17,style=ButtonStyle(shape={
        '':RoundedRectangleBorder(radius=7),},overlay_color={'':'transparent'},),),
        Text(value=text,color=c.pink17,size=20,opacity=1,animate_opacity=200)]),)

    def build(self):
        return Container(width=200,height=1000,
        padding=padding.only(top=2),alignment=alignment.top_left,
        content=Column(horizontal_alignment='center',
        controls=[self.user.build(),Container(width=24,
        height=24,content=Row(controls=[IconButton(
        icon=icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED,icon_size=18,
        icon_color=c.pink17,style=ButtonStyle(
        shape={'': RoundedRectangleBorder(radius=7)},
        overlay_color={'': 'transparent'},)
        ,on_click=partial(self.func))]), ),
        Divider(height=5,color='transparent'),
        self.ContainedIcons(icons.HOME,'Home','home'),
        self.ContainedIcons(icons.WAVES_SHARP, 'Generate','generate'),
        self.ContainedIcons(icons.LIBRARY_MUSIC, 'Library','lib'),
        self.ContainedIcons(icons.NOTIFICATIONS, 'Notifications','notification'),
        self.ContainedIcons(icons.ACCOUNT_BALANCE_WALLET, 'Go to PRO','pro'),
        Divider(height=2.5,color=c.pink17),
        self.ContainedIcons(icons.LOGOUT_ROUNDED, 'Log out','logout'),]))

