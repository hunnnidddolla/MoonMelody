from flet import *
import colors as c
textbasic1='            Basic'
textbasic2='''Music generation from 
text prompts up to 1 minutes'''
textbasic3='''Access to a limited number 
of styles and genres 
(up to 5 popular genres)'''
textbasic4='Maximum of 10 tracks per month'
textbasic5='''Standard audio quality 
(128 kbps)'''
textbasic6='''No access to 
the library of ready-made tracks

'''
text='                      '
text1='                                    per month'

class GoToProPage(UserControl):
    def __init__(self):
        super().__init__()
        self.page = page
        self.page.route = '/pro'
        self.basic = Container(margin=10,border_radius=10,padding=padding.all(5),
        bgcolor='surface,0.1',height=600,content=Column(controls=[
        Row(controls=[Text(value=textbasic1, size=30, color=c.pink17)],alignment='center'),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED,size=15,color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic2, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic3, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic4, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic6, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic5, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Row(controls=[Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
        Text(value=textbasic6, size=15,color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
        Divider(height=1.5,color='transparent'),
        Row(controls=[Text(text),Text(value='FREE', size=35, color=c.pink17)],alignment='center'),
        Row(controls=[Text(value=text1, size=10, color=c.pink17)],alignment=alignment.center),
        Divider(height=6, color='transparent'),Row(controls=[Text(text),
        ElevatedButton(content=Text(value='Selecet',size=15,color=c.pink17),bgcolor='surface,0.01',)],alignment='center'),
        Divider(height=30, color='transparent'),],alignment='center'))
        self.standart = Container(
            margin=10,
            height=600,
            border_radius=10,
            padding=padding.all(10),
            bgcolor='surface,0.3',
            content=Column(controls=[
                Row(controls=[Text(value='           Standard', size=30, color=c.pink17)],
                    alignment='center'),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Music generation from 
text prompts up to 5 minutes''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Access to a limited number 
of styles and genres 
(up to 15 popular genres)''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='Maximum of 30 tracks per month', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Standard audio quality 
(320 kbps)''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Extended support 
(email and chat, 
response within 24 hours))''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Access to the library of ready-made 
tracks with the ability 
to download up to 20 tracks per month''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Divider(height=1.5, color='transparent'),
                Row(controls=[Text('                   '), Icon(name=icons.ATTACH_MONEY, size=35, color=c.pink17),
                              Text(value='5.5', size=35, color=c.pink17)],
                    alignment='center'),
                Row(controls=[Text(value='                                    per month', size=10, color=c.pink17)],
                    alignment=alignment.center),
                Divider(height=1.5, color='transparent'),
                Row(controls=[Text('                  '),
                              ElevatedButton(content=Text(value='Selecet', size=15, color=c.pink17),
                                             bgcolor='surface,0.01', )], alignment='center'),
                Divider(height=30, color='transparent'),
            ],
                alignment='center')
        )
        self.pro = Container(
            margin=10,
            height=600,
            border_radius=10,
            padding=padding.all(10),
            bgcolor='surface,0.5',
            content=Column(controls=[
                Row(controls=[Text(value='            PRO', size=30, color=c.pink17)],
                    alignment='center'),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Music generation from 
text prompts without time limits''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Full access to all styles and genres''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='Unlimited number of tracks per month', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Highest audio quality (lossless)''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Premium support 
(email, chat, and phone, 
response within 12 hours)''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Full access to the library 
of ready-made tracks with 
unlimited downloads ''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Row(controls=[
                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=15, color=colors.with_opacity(0.7, c.pink17)),
                    Text(value='''Commercial use rights with 
full ownership of created tracks''', size=15,
                         color=colors.with_opacity(0.7, c.pink17))], alignment=alignment.top_center),
                Divider(height=2, color='transparent'),
                Row(controls=[Text('                   '), Icon(name=icons.ATTACH_MONEY, size=35, color=c.pink17),
                              Text(value='10', size=35, color=c.pink17)],
                    alignment='center'),
                Row(controls=[Text(value='                                    per month', size=10, color=c.pink17)],
                    alignment=alignment.center),
                Divider(height=1.5, color='transparent'),
                Row(controls=[Text('                  '),
                              ElevatedButton(content=Text(value='Selecet', size=15, color=c.pink17),
                                             bgcolor='surface,0.01', )], alignment='center'),
                Divider(height=30, color='transparent'),
            ],
                alignment='center')
        )

    def build(self):
        return Row(
            controls=[ Column(
               controls=[
                    self.basic
               ]
            ),
                Column(
                    controls=[
                        self.standart
                    ]
                ),
                Column(
                    controls=[
                        self.pro
                    ]
                ),

            ]
        )


