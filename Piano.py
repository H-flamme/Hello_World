WIDTH = 735
HEIGHT = 99

do0 = [Actor('do_1'),Actor('re_1'),Actor('mi_1'),Actor('fa_1'),Actor('sol_1'),Actor('la_1'),Actor('si_1'),
Actor('do_2'),Actor('re_1'),Actor('mi_1'),Actor('fa_1'),Actor('sol_1'),Actor('la_1'),Actor('si_1'),
Actor('do_3'),Actor('re_1'),Actor('mi_1'),Actor('fa_1'),Actor('sol_1'),Actor('la_1'),Actor('si_1'),
Actor('do_4'),Actor('re_1'),Actor('mi_1'),Actor('fa_1'),Actor('sol_1'),Actor('la_1'),Actor('si_1'),
Actor('do_5'),Actor('re_1'),Actor('mi_1'),Actor('fa_1'),Actor('sol_1'),Actor('la_1'),Actor('si_1')]

do_diese = Actor('do_diese_1')
notes = [sounds.A_1,sounds.A_2,sounds.A_3,sounds.A_4,sounds.A_5,sounds.A_6,sounds.A_7,
sounds.B_1,sounds.B_2,sounds.B_3,sounds.B_4,sounds.B_5,sounds.B_6,sounds.B_7,
sounds.C_1,sounds.C_2,sounds.C_3,sounds.C_4,sounds.C_5,sounds.C_6,sounds.C_7,
sounds.D_1,sounds.D_2,sounds.D_3,sounds.D_4,sounds.D_5,sounds.D_6,sounds.D_7,
sounds.E_1,sounds.E_2,sounds.E_3,sounds.E_4,sounds.E_5,sounds.E_6,sounds.E_7]

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