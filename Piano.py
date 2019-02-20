WIDTH = 735
HEIGHT = 99

do = [Actor('do_0'),Actor('la_0')]
do_diese = Actor('do_diese_1')
notes = [sounds.do,sounds.re]

def draw():
    screen.fill((254,254,254))
    for valeur in range(2):
        do[valeur].pos = 10 + valeur * 21,50
        do[valeur].draw()

def on_mouse_down(pos):
    for valeur in range(2):
        if do[valeur].collidepoint(pos):
            print("touché")
            notes[valeur].play()