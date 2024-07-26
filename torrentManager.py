# torrent_manager.py
import threading
import random
import time

class TorrentManager:
    def __init__(self, torrent_file, max_peers, update_ui_callback=None):
        self.torrent_file = torrent_file
        self.max_peers = max_peers
        self.update_ui_callback = update_ui_callback
        self.peers = []
        self.download_progress = 0

    def start_server(self):
        self._log("Server started")
        while True:
            time.sleep(1)  # Placeholder para a execução do servidor

    def add_peer(self, ip, port):
        if len(self.peers) < self.max_peers:
            self.peers.append((ip, port))
            self._log(f"Added peer {ip}:{port}")
        else:
            self._log("Max peers reached")

    def get_peers(self):
        return self.peers

    def start_download(self):
        self._log("Download started")
        self.download_progress = 0
        while self.download_progress < 100:
            time.sleep(1)
            self.download_progress += random.randint(1, 5)  # Simulação de progresso de download
            self._log(f"Download progress: {self.download_progress}%")
            if self.update_ui_callback:
                self.update_ui_callback(f"Download progress: {self.download_progress}%")
        self._log("Download completed")

    def get_download_progress(self):
        return self.download_progress

    def start_upload(self):
        self._log("Upload started")
        while True:
            time.sleep(1)  # Placeholder para a execução do upload

    def _log(self, message):
        if self.update_ui_callback:
            self.update_ui_callback(message)
        print(message)
