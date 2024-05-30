from flet import *
import colors as c
from db import supabase
from random import choice

class LibraryPage(UserControl):
    def __init__(self, user_id: str):
        super().__init__()

        self.user_id = user_id
        self.discription = Container(
            padding=padding.only(top=10,bottom=10),
            bgcolor='transparent',
            content=
                Row(controls=[Text(value='                       Library', size=50, color=c.pink17)],
                    alignment='center')

        )
        self.filepicker=FilePicker()
        self.playlist = supabase.storage.from_('User_generation').list(path=f'{self.user_id}')
        self.playlist_url = [supabase.storage
                             .from_('User_generation')
                             .get_public_url(f"{self.user_id}/{x['name']}")
                             for x in self.playlist]
        self.images = [f'img/{x}.jpeg' for x in range(1, 12)]
        self.playlist_content = [
            Container(padding=padding.all(5),content=Column(
            controls=[Stack(controls=[
            Image(src=choice(self.images), width=100, height=100, border_radius=10, color_blend_mode=c.pink17),
            Column(controls=[IconButton(icon=icons.PLAY_CIRCLE_FILL_ROUNDED,
            icon_color=colors.with_opacity(0.5, c.pink17),icon_size=85,
            on_click=lambda e, url_=url: self.play_audio(url_))],alignment='center')], alignment='center'),
            Row(controls=[Text(value=track['name'].replace('.wav', ''), color=c.pink17, size=20),
            IconButton(icon=icons.DOWNLOAD_FOR_OFFLINE_ROUNDED,icon_color=c.pink17,icon_size=20,
            on_click=lambda e, filename=track['name']: self.navigate_to_directory_selection(filename))]),])
            ) for track, url in zip(self.playlist, self.playlist_url)]
    def play_audio(self, src: str):
        audio = Audio(src=src, autoplay=True, volume=1, balance=0)
        self.page.overlay.append(audio)
        self.page.update()
    def navigate_to_directory_selection(self, filename: str):
        self.page.client_storage.set("current_file_to_download", filename)
        self.page.go("/select_directory")
    def build(self):
        return Container(content=Column(controls=[self.discription, Row(controls=self.playlist_content)]))




