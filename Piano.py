WIDTH = 735
HEIGHT = 99

do0 = [Actor('do_0'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_1'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_2'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_3'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_4'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('la_0'),Actor('mi_&0'),Actor('fa_0')]

do_diese = Actor('do_diese_1')
notes = [sounds.C_1,sounds.D_1,sounds.E_1,sounds.F_1,sounds.G_1,sounds.A_1,sounds.B_1,
sounds.C_2,sounds.D_2,sounds.E_2,sounds.F_2,sounds.G_2,sounds.A_2,sounds.B_2,
sounds.C_3,sounds.D_3,sounds.E_3,sounds.F_3,sounds.G_3,sounds.A_3,sounds.B_3,
sounds.C_4,sounds.D_4,sounds.E_4,sounds.F_4,sounds.G_4,sounds.A_4,sounds.B_4,
sounds.C_5,sounds.D_5,sounds.E_5,sounds.F_5,sounds.G_5,sounds.A_5,sounds.B_5]

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