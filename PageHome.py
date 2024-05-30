from flet import*
import colors as c
#done

text1='                  Moon Melody                '
text2='''    
    Create unique music from text prompts with our innovative application.     
    Moon Melody offers a simple and intuitive interface that allows you to     
    easily generate tracks inspired by your ideas.     
    Discover new sounds, create playlists, and share your music with friends.    '''
text3='''    
    Key features of Moon Melody:

    _ Generate music from text prompts
    _ Save and manage your tracks in the library
    _ Notifications about new features and updates
    _ Access premium features with a Go Pro subscription
    
    Start your musical journey with Moon Melody today!
    
    '''
class HomePage(UserControl):
    def __init__(self):
        super().__init__()
        self.page=page
        self.page.route='/home'
        self.discription= Container(margin=10,
        bgcolor='transparent',content=Column(controls=[
        Row(controls=[Text(value=text1,size=50,color=c.pink17)],alignment=alignment.top_center),
        Row(controls=[Text(value=text2, size=25, color=colors.with_opacity(0.7,c.pink17))],
        alignment=alignment.top_center),
        Row(controls=[Text(value=text3,size=25,color=colors.with_opacity(0.7,c.pink17))]),
        ],alignment='center'))
    def build(self):
        return Column(
            controls=[
                self.discription
            ]
        )




