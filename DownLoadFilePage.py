from db import supabase
from flet import*
import colors as c
class DirectorySelectionPage(UserControl):
    def __init__(self):
        super().__init__()
        self.filepicker = FilePicker(on_result=self.on_directory_selected)
    def on_directory_selected(self, e):
        if e.path:
            self.page.client_storage.set("selected_directory", e.path)
            print("Directory saved to client_storage",self.page.client_storage.get("selected_directory"))
            e.page.go("/lib")
    def build(self):
        return Column(alignment='center',controls=[Text("Select directory to download file",
            size=30,color=c.pink17),ElevatedButton(content=Row(controls=[
            Text(value="Select Directory",color=c.pink17,size=20),
            Icon(name=icons.FOLDER,color=c.pink17, size=20)]),
                on_click=lambda _: self.filepicker.get_directory_path(),bgcolor='transparent')])

class FileDownloadManager:
    @staticmethod
    def download_file(page, user_id):
        selected_directory = page.client_storage.get("selected_directory")
        current_file_to_download = page.client_storage.get("current_file_to_download")
        if selected_directory and current_file_to_download:
            source_path = f"{user_id}/{current_file_to_download}"
            destination_path = f"{selected_directory}\\{current_file_to_download}"
            res = supabase.storage.from_('User_generation').download(source_path)
            if res:
                with open(destination_path, 'wb+') as f:
                    f.write(res)
                print(f"File {current_file_to_download} downloaded successfully to {destination_path}.")
            else:
                print(f"Failed to download file {current_file_to_download}.")
        else:
            print("No directory selected for download.")
