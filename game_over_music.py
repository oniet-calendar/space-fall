from pygame import mixer

def gameOverMusic(a):
    if(a == 0):
        mixer.init()
        mixer.music.load('./sounds/game-over.mp3')
        mixer.music.play()
        mixer.music.set_volume(0.7)