import pygame
import threading

pygame.mixer.init()

def play_sound(file_path):
    def _play():
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    threading.Thread(target=_play).start()

def play_bell():
    play_sound("server/sounds/bell.mp3")

def play_anthem():
    play_sound("server/sounds/istiklal_marsi.mp3")
