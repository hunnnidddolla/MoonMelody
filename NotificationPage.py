from flet import *

import colors as c

#done
#Notification
text='                      Notification               '
class NotificationsPage(UserControl):
    def __init__(self):
        super().__init__()
        self.page = page
        self.page.route = '/notifications'
        self.discription = Container(padding=padding.only(top=10),
        bgcolor='transparent',content=Column(controls=[
        Row(controls=[Text(value=text, size=50, color=c.pink17)],
        alignment=alignment.top_center)], alignment='center'))
        self.card=Container(bgcolor='surface,0.1',width=800,
        expand=True,border_radius=10,content=Column(controls=[
        Container(content=Row(controls=[Rive(
        src='Animation/scrolling_letter.riv',fit=ImageFit.COVER,width=150,height=150),
        Text(value=' Subscribe to our newsletter! ',color=c.pink17,size=40)],alignment='center')),
        Container(content=Column(controls=[Row(controls=[
        Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=25, color=c.pink17),
        Text(value='Get updates on the latest tools and functionalities.',color=c.pink17,size=25)
        ],alignment='center')
            ,
                            Row(
                                controls=[
                                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=25, color=c.pink17),
                                    Text(value='Receive special discounts and promotions.', color=c.pink17,
                                         size=25)
                                ],alignment='center'
                            ),
                            Row(
                                controls=[
                                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=25, color=c.pink17),
                                    Text(value='Learn from expert advice and tutorials.', color=c.pink17,
                                         size=25)
                                ],alignment='center'
                            ),
                            Row(
                                controls=[
                                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=25, color=c.pink17),
                                    Text(value='Stay connected with the Moon Melody community.', color=c.pink17,
                                         size=25)
                                ],alignment='center'
                            ),
                            Row(
                                controls=[
                                    Icon(name=icons.FAVORITE_BORDER_ROUNDED, size=25, color=c.pink17),
                                    Text(value="Don't miss out on our webinars, workshops, and more.", color=c.pink17,
                                         size=25)
                                ],alignment='center'
                            ),
                            Divider(height=10,color='transparent'),
                            Row(alignment='center',controls=[ElevatedButton(
                                width=250,
                                height=70,
                                bgcolor='transparent',
                                content=Row(
                                    controls=[
                                        Rive(
                                            src='Animation/logo (4).riv', fit=ImageFit.COVER, width=50,
                                            height=50,
                                        ),
                                        Text(value="Subscribe",
                                             color=c.pink17,
                                             size=25)
                                    ]
                                )

                            )]),
                                Divider(height=10, color='transparent'),
                        ]
                    ),

                    )
                ]
            )


        )

    def build(self):
        return Column(
            controls=[
                self.discription,
                Container(
                    padding=padding.only(left=100,top=10),
                    content=self.card
                )
            ]
        )
