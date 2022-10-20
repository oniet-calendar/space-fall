from pygame import mixer

def combo_sfx():
    combo = mixer.Sound('./sounds/combo.mp3')
    combo.play()