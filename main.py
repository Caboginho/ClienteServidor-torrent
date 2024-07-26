# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import threading
from torrent_manager import TorrentManager  # Importa o TorrentManager

class MainScreen(Screen):
    pass

class TorrentApp(MDApp):
    def build(self):
        self.torrent_manager = TorrentManager("example.torrent", 10, update_ui_callback=self.update_ui)
        return Builder.load_file("main.kv")

    def start_server(self):
        try:
            self.log_message("Starting server...")
            server_thread = threading.Thread(target=self.torrent_manager.start_server)
            server_thread.start()
        except Exception as e:
            self.log_message(f"Error: {e}")

    def add_peer(self):
        try:
            ip = "127.0.0.1"  # Placeholder IP, replace with actual input
            port = 6881       # Placeholder port, replace with actual input
            self.torrent_manager.add_peer(ip, port)
            self.log_message(f"Added peer {ip}:{port}")
        except Exception as e:
            self.log_message(f"Error: {e}")

    def start_download(self):
        try:
            torrent_file = self.root.ids.main_screen.ids.torrent_file.text
            self.torrent_manager.torrent_file = torrent_file
            self.log_message(f"Starting download for {torrent_file}")
            download_thread = threading.Thread(target=self.torrent_manager.start_download)
            download_thread.start()
        except Exception as e:
            self.log_message(f"Error: {e}")

    def start_upload(self):
        try:
            torrent_file = self.root.ids.main_screen.ids.torrent_file.text
            self.torrent_manager.torrent_file = torrent_file
            self.log_message(f"Starting upload for {torrent_file}")
            upload_thread = threading.Thread(target=self.torrent_manager.start_upload)
            upload_thread.start()
        except Exception as e:
            self.log_message(f"Error: {e}")

    def show_peers(self):
        try:
            peers = self.torrent_manager.get_peers()
            self.log_message(f"Connected peers: {peers}")
        except Exception as e:
            self.log_message(f"Error: {e}")

    def show_progress(self):
        try:
            progress = self.torrent_manager.get_download_progress()
            self.log_message(f"Download progress: {progress}%")
        except Exception as e:
            self.log_message(f"Error: {e}")

    def log_message(self, message):
        self.root.ids.main_screen.ids.log_label.text = message

    def update_ui(self, message):
        self.log_message(message)

if __name__ == '__main__':
    TorrentApp().run()
