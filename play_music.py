from pygame import mixer

def play_music():
    mixer.init()
    mixer.music.unload
    mixer.music.load('./sounds/space-fall-playing.wav')
    mixer.music.play(loops=50,fade_ms=1200)
    mixer.music.set_volume(0.5)