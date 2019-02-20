WIDTH = 735
HEIGHT = 99

do0 = [Actor('do_0'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_1'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_2'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_3'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_4'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('la_0'),Actor('mi_0'),Actor('fa_0')]
do_diese = [25]

notes = [sounds.a_1,sounds.a_2,sounds.a_3,sounds.a_4,sounds.a_5,sounds.a_6,sounds.a_7,
sounds.b_1,sounds.b_2,sounds.b_3,sounds.b_4,sounds.b_5,sounds.b_6,sounds.b_7,
sounds.c_1,sounds.c_2,sounds.c_3,sounds.c_4,sounds.c_5,sounds.c_6,sounds.c_7,
sounds.d_1,sounds.d_2,sounds.d_3,sounds.d_4,sounds.d_5,sounds.d_6,sounds.d_7,
sounds.e_1,sounds.e_2,sounds.e_3,sounds.e_4,sounds.e_5,sounds.e_6,sounds.e_7]
place = 0

def draw():
    screen.fill((254,254,254))
    for valeur in range(25):
        do_diese[valeur] = Actor('do_diese_1')
    for valeur in range(35):
        do0[valeur].pos = 10 + valeur * 21,50
        do0[valeur].draw()
    for valeur1 in range(5):
        for valeur in range(2):
            do_diese[place].pos = 20 + valeur * 21 + valeur1 * 147,25
            do_diese[place].draw()
            place += 1
        for valeur in range(3):
            do_diese[place].pos = (20 + valeur * 21 + 63.75) + valeur1 * 147,25
            do_diese[place].draw()
            place += 1
def on_mouse_down(pos):
    musics = 0
    for valeur in range(25):
        if do_diese[valeur].collidepoint(pos):

            musics = 0
        else:
            musics = 1
    if musics == 1:
        for valeur in range(35):
            if do0[valeur].collidepoint(pos):
                notes[valeur].play()