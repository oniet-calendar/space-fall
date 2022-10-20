from pygame import mixer

def jump_sfx():
    combo = mixer.Sound('./sounds/jump.mp3')
    combo.play()