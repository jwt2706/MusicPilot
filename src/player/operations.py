import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None

    def load(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        self.current_track = file_path
        pygame.mixer.music.load(file_path)

    def play(self):
        if self.current_track:
            pygame.mixer.music.play()
        else:
            print("No track loaded.")

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()