from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('./sounds/space-fall-theme.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.7)