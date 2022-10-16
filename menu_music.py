from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('./sounds/space-fall-theme.mp3')
    mixer.music.play(loops=25,fade_ms=700)
    mixer.music.set_volume(0.7)