from flet import*
from MainWindow import MainWindow
from RegistrationWindow import Register_Window,MainFromUI
from db import supabase
from PageHome import HomePage
from CustPage import CustomPage
from NotificationPage import NotificationsPage
from GotoPro import GoToProPage
from PageGenerate import PageGenerate
from db import supabase
import colors as c
from libraryPage import LibraryPage
from DownLoadFilePage import DirectorySelectionPage,FileDownloadManager
def show_logout_confirmation_dialog(page: Page):
    def on_yes(e):
        supabase.auth.sign_out()
        page.client_storage.remove('current_user')
        page.go("/")
        page.dialog.open = False
        page.update()
    def on_no(e):
        page.dialog.open = False
        page.update()
    page.dialog = AlertDialog(modal=True,
    title=Text("Confirmation"),content=Text("Are you sure you want to log out?"),
    actions=[ElevatedButton(text="Yes", on_click=on_yes),
    ElevatedButton(text="No", on_click=on_no)],actions_alignment=MainAxisAlignment.END,)
    page.dialog.open = True
def main(page:Page):
    page.title = 'Moon Melody'
    page.theme_mode = ThemeMode.DARK
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    form = CustomPage(page)
    page.fonts = {'CustomFont': 'Fonts/Bardo.otf'}
    page.theme = Theme(font_family='CustomFont')
    current_user = page.client_storage.get('current_user')

    if current_user:
        page.go("/home")
    else:
        page.go("/auth")
    def route_change(e) -> None:
        page.overlay.clear()
        if e.route=='/':
            page.overlay.append(Stack(controls=[Rive(
        src='Animation/bg.riv', fit=ImageFit.COVER),
        Container(content=MainWindow(),alignment=alignment.center)],
        alignment='center'))
        elif e.route == "/auth":
            page.overlay.append(Stack(controls=[Rive(
        src='Animation/bg.riv', fit=ImageFit.COVER),
        Container(content=MainFromUI(supabase),alignment=alignment.center)],
        alignment='center'))
        elif e.route == "/register":
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),
            Container(content=Register_Window(supabase),alignment=alignment.center)],
            alignment='center'))
        elif e.route=='/generate':
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER, ),Card(
            color='transparent',content=Row(controls=[
            form,VerticalDivider(width=1, color='transparent'),
            Container(content=PageGenerate(page),width=1000,
            height=900,bgcolor='transparent',border_radius=10)
            ], vertical_alignment=MainAxisAlignment.CENTER,) )]))
        elif e.route == "/home":
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),Card(
            color='transparent',content=Row(controls=[
            form,VerticalDivider(width=1, color='transparent'),
            Container(content=HomePage(),bgcolor='transparent',
            border_radius=10)], vertical_alignment=MainAxisAlignment.CENTER,))]))
        elif e.route == "/lib":
            page.overlay.clear()
            user_id = e.page.client_storage.get('current_user')
            FileDownloadManager.download_file(page, user_id)
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),
            Card(color='transparent',content=Row(controls=[
            form,VerticalDivider(width=1, color='transparent'),
            Container(content=LibraryPage(user_id=user_id),bgcolor='transparent',
            border_radius=10 )], vertical_alignment=MainAxisAlignment.CENTER,))]
            ))
        elif e.route == "/notification":
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),Card(
            color='transparent',content=Row(controls=[
            form,VerticalDivider(width=1, color='transparent'),
            Container(content=NotificationsPage(),bgcolor='transparent',
            border_radius=10)], vertical_alignment=MainAxisAlignment.CENTER,))]
            ))
        elif e.route=='/pro':
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),Card(
            color='transparent',content=Row(controls=[form,
            VerticalDivider(width=1, color='transparent'),
            Container(content=GoToProPage(),bgcolor='transparent',
            border_radius=10 )], vertical_alignment=MainAxisAlignment.CENTER,))]))
        elif e.route=='/select_directory':
            directory_selection_page = DirectorySelectionPage()
            page.overlay.clear()
            page.overlay.append(Stack(controls=[Rive(
            src='Animation/bg.riv', fit=ImageFit.COVER),Card(
            color='transparent',content=Row(controls=[
            form,VerticalDivider(width=1, color='transparent'),
            Container(content=directory_selection_page,bgcolor='transparent',
            border_radius=10)], vertical_alignment=MainAxisAlignment.CENTER,)
            )]))


            page.overlay.append(
                directory_selection_page.filepicker)
        elif e.route=='/logout':
            show_logout_confirmation_dialog(page)


        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.go("/")
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.update()

if __name__ == '__main__':
    app(target=main,assets_dir='src')

