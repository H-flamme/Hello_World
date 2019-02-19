WIDTH = 734
HEIGHT = 99

def draw():
    for valeur in range(4):
        screen.blit("do_" + valeur,(0 + 21 * valeur,0))
