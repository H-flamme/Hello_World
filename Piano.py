WIDTH = 735
HEIGHT = 99

do0 = [Actor('do_0'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_1'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_2'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_3'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_4'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('la_0'),Actor('mi_0'),Actor('fa_0')]

do_diese = Actor('do_diese_1')
notes = [sounds.do,sounds.la,sounds.mi,sounds.fa,sounds.la,sounds.la,sounds.mi,
sounds.do,sounds.la,sounds.mi,sounds.fa,sounds.la,sounds.la,sounds.mi,
sounds.do,sounds.la,sounds.mi,sounds.fa,sounds.la,sounds.la,sounds.mi,
sounds.do,sounds.la,sounds.mi,sounds.fa,sounds.la,sounds.la,sounds.mi,
sounds.do,sounds.la,sounds.mi,sounds.fa,sounds.la,sounds.la,sounds.mi]

def draw():
    screen.fill((254,254,254))
    for valeur in range(35):
        do0[valeur].pos = 10 + valeur * 21,50
        do0[valeur].draw()
    for valeur1 in range(5):
        for valeur in range(2):
            do_diese.pos = 20 + valeur * 21 + valeur1 * 147,25
            do_diese.draw()
        for valeur in range(3):
            do_diese.pos = (20 + valeur * 21 + 63.75) + valeur1 * 147,25
            do_diese.draw()

def on_mouse_down(pos):
    for valeur in range(35):
        if do0[valeur].collidepoint(pos):
            notes[valeur].play()