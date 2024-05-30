from flet import*
import colors as c
from db import supabase
class UserData():
    def __init__(self,initials: str, name: str, description: str):
        self.name = name
        self.initials = initials
        self.description = description
    def build(self):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=50, height=50, bgcolor=colors.with_opacity(0.2,c.pink17), alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=self.initials,
                            size=30,
                            weight='bold',
                            color=c.pink17),),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(
                                color=c.pink17,
                                value=self.name,
                                size=20,
                                weight='bold',
                                opacity=1,
                                animate_opacity=200
                            ),
                            Text(
                        value=self.description,
                                size=12,
                                color=c.pink17,
                                weight='w400',
                                opacity=1,
                                animate_opacity=200
                            ),

                        ]
                    )
                ]
            )
        )
def create_user_folder(self,user_id: str):
    folder_path = f"{user_id}/placeholder.txt"
    response = supabase.storage.from_("User_generation").upload(folder_path, "")

    if response.status_code == 200:
        print(f"Folder created for user {user_id}")
    else:
        print(f"Failed to create folder for user {user_id}: {response.content}")



