from flet import*
import colors as c
text1='Welcome to Moon Melody'
text2='"The Harmony of Your Words"'
text3='''  Our innovative platform allows you to generate unique melodies from your textual prompts, creating
  a harmonious blend of creativity and technology.
    How It Works:'''
text4='''   ♪ Enter a textual prompt or phrase that inspires you.
   ♪ Our advanced algorithm interprets your input and generates a custom melody.
   ♪ Listen, edit, and perfect your creation.'''
text5='''  Whether you're a songwriter looking for inspiration, a music enthusiast, or just curious, Moon Melody 
  offers a new way to experience the power of words and music. Start creating your harmony today!'''
class MainWindow(UserControl):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.page = page
        self.route = '/mainwnd'
        self.title=Row(controls=[Text(value=text1,size=60,color=c.pink20)],alignment='center')
        self.slogan=Row(controls=[Text(value=text2,size=30,color=c.pink20,style=TextStyle(italic=True))],
                        alignment='center' )
        self.text1=Row(controls=[Text(value=text3, size=20, color=c.pink13)],alignment=alignment.top_right)
        self.text2=Row(controls=[Text(value=text4, size=20, color=c.pink13)],alignment=alignment.top_right)
        self.text3=Row(controls=[Text(value=text5, size=20, color=c.pink13)],alignment=alignment.top_right)
        self.btn=Row(controls=[ElevatedButton(width=170,height=45,content=Row([
        Icon(name=icons.STARS_SHARP, color=c.pink16),Text(value='Get start', size=18, color=c.pink16)]),
        bgcolor=c.pink17,on_click=lambda e: e.page.go('/auth'),
        on_hover=lambda e: self.Highlight(e),)],alignment='center')
    def Highlight(self, e):
        if e.data == 'true':
            e.control.border_color = c.pink15,
            e.control.shadow = BoxShadow(
                spread_radius=6,
                blur_radius=8,
                color=colors.with_opacity(0.25, 'black'),
                offset=Offset(4, 4)
            )

            e.control.bgcolor = c.pink17
            e.control.update()
            e.control.content.controls[0].icon_color = c.pink13
            e.control.content.controls[1].color = c.pink13
            e.control.content.update()
        else:
            e.control.bgcolor = c.pink17
            e.control.update()

            e.control.content.controls[0].icon_color = c.pink16
            e.control.content.controls[1].color = c.pink16
            e.control.content.update()

    def build(self):
        return Card(
            color= 'transparent',margin=10,
            shadow_color=colors.with_opacity(0.02,c.pink19),
            width=1000,height=700,shape=RoundedRectangleBorder(radius=7),
            content=Container(alignment=alignment.center,content=Column(
                expand=True,controls=[self.title,self.slogan,Divider(height=5, color='transparent'),
                self.text1,Divider(height=5,color='transparent'),self.text2,
                Divider(height=5, color='transparent'),self.text3,
                Divider(height=10, color='transparent'),self.btn],alignment='center'
         )),)




