import pygame

def play_bgm():
    pygame.init()
    pygame.mixer.init()

    sound = pygame.mixer.Sound("/home/zeno/Desktop/Jarvis/mp3(data)/X2Download.app - Tony's Workshop Music — Productivity Superhero Mix (128 kbps).mp3")
    sound.set_volume(0.1)

    sound.play()

    while pygame.mixer.get_busy():
     pass

    pygame.quit()


