import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import subprocess
import platform
from player.operations import MusicPlayer

class MusicPlayerUI:
    def __init__(self, root):
        self.root = root
        self.player = MusicPlayer()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("MusicPilot")

        # Create a style object
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 16))
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TCanvas", background="white")

        # Create a label for the title
        title_label = ttk.Label(self.root, text="MusicPilot", style="TLabel")
        title_label.pack(pady=10)

        # Create a canvas for the custom progress bar
        self.canvas = tk.Canvas(self.root, width=400, height=50, bg="white")
        self.canvas.pack(pady=10)

        # Draw the progress bar line
        self.progress_line = self.canvas.create_line(10, 25, 390, 25, fill="gray", width=2)

        # Draw the draggable circle
        self.circle = self.canvas.create_oval(0, 15, 20, 35, fill="blue")

        # Bind mouse events to the circle
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.move_circle)
        self.canvas.tag_bind(self.circle, "<Button-1>", self.click_circle)

        # Create buttons for pause/resume, load, and open file explorer
        self.pause_resume_button = ttk.Button(self.root, text="Pause", command=self.pause_resume_music, style="TButton")
        self.pause_resume_button.pack(pady=10)

        load_button = ttk.Button(self.root, text="Load Audio", command=self.open_file_dialog, style="TButton")
        load_button.pack(pady=10)

        open_explorer_button = ttk.Button(self.root, text="Open File Explorer", command=self.open_file_explorer, style="TButton")
        open_explorer_button.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select an Audio File",
            filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*"))
        )
        if file_path:
            self.player.load(file_path)
            self.player.play()
            self.update_scale()

    def open_file_explorer(self):
        system = platform.system()
        if system == "Windows":
            subprocess.run(["explorer", "."])
        elif system == "Darwin":  # macOS
            subprocess.run(["open", "."])
        elif system == "Linux":
            subprocess.run(["xdg-open", "."])
        else:
            print(f"Unsupported OS: {system}")

    def stop_music(self):
        self.player.stop()

    def pause_resume_music(self):
        if self.player.is_playing():
            self.player.pause()
            self.pause_resume_button.config(text="Resume")
        else:
            self.player.unpause()
            self.pause_resume_button.config(text="Pause")

    def update_scale(self):
        if self.player.current_track:
            current_pos = self.player.get_pos() / 1000  # get_pos() returns milliseconds
            total_duration = self.player.get_length() / 1000  # get_length() returns milliseconds
            self.current_time_label.config(text=self.format_time(current_pos))
            self.total_duration_label.config(text=self.format_time(total_duration))
            self.move_circle_to_position(current_pos / total_duration)
        self.root.after(1000, self.update_scale)  # update every second

    def move_circle(self, event):
        x = event.x
        if 10 <= x <= 390:
            self.canvas.coords(self.circle, x-10, 15, x+10, 35)
            self.player.play(start=(x-10) / 380 * self.player.get_length() / 1000)

    def click_circle(self, event):
        self.move_circle(event)

    def move_circle_to_position(self, position):
        x = 10 + position * 380
        self.canvas.coords(self.circle, x-10, 15, x+10, 35)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"