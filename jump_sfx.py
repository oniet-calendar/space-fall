from pygame import mixer

def jump_sfx():
    combo = mixer.Sound('./sounds/jump.mp3')
    combo.set_volume(0.5)
    combo.play()