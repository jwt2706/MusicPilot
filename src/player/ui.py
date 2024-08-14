import tkinter as tk
from tkinter import filedialog
from player.operations import MusicPlayer

class MusicPlayerUI:
    def __init__(self, root):
        self.root = root
        self.player = MusicPlayer()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Music Player")

        # Create a label
        label = tk.Label(self.root, text="Music Player")
        label.pack(pady=10)

        # Create buttons
        load_button = tk.Button(self.root, text="Load and Play", command=self.open_file_dialog)
        load_button.pack(pady=10)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        stop_button.pack(pady=10)

        pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        pause_button.pack(pady=10)

        unpause_button = tk.Button(self.root, text="Unpause", command=self.unpause_music)
        unpause_button.pack(pady=10)

        # Create a scale for the player bar
        self.scale = tk.Scale(self.root, from_=0, to=100, orient='horizontal', command=self.on_scale_move)
        self.scale.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*"))
        )
        if file_path:
            self.player.load(file_path)
            self.player.play()
            self.update_scale()

    def stop_music(self):
        self.player.stop()

    def pause_music(self):
        self.player.pause()

    def unpause_music(self):
        self.player.unpause()

    def update_scale(self):
        # Implement logic to update the scale based on the music progress
        pass

    def on_scale_move(self, val):
        # Implement logic to handle scale movement
        pass