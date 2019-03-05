import time

WIDTH = 735
HEIGHT = 99

do_grave = [0,1,2,3,4,5,6]
do_peu_grave = [7,8,9,10,11,12,13]
do_normal = [14,15,16,17,18,19,20]
do_peu_aigu = [21,22,23,24,25,26,27]
do_aigu = [28,29,30,31,32,33,34]

do0 = [Actor('do_0'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_1'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_2'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_3'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('do_4'),Actor('la_0'),Actor('mi_0'),Actor('fa_0'),Actor('la_0'),Actor('la_0'),Actor('mi_0'),
Actor('la_0'),Actor('mi_0'),Actor('fa_0')]

do_diese = []
do_diese1 = Actor('do_diese_1')
toucheEnfonce = Actor('touche_enfonce')

notes = [sounds.a_1,sounds.a_2,sounds.a_3,sounds.a_4,sounds.a_5,sounds.a_6,sounds.a_7,
sounds.b_1,sounds.b_2,sounds.b_3,sounds.b_4,sounds.b_5,sounds.b_6,sounds.b_7,
sounds.c_1,sounds.c_2,sounds.c_3,sounds.c_4,sounds.c_5,sounds.c_6,sounds.c_7,
sounds.d_1,sounds.d_2,sounds.d_3,sounds.d_4,sounds.d_5,sounds.d_6,sounds.d_7,
sounds.e_1,sounds.e_2,sounds.e_3,sounds.e_4,sounds.e_5,sounds.e_6,sounds.e_7]

notes_diese = [sounds.a_1_5,sounds.a_2_5,sounds.a_4_5,sounds.a_5_5,sounds.a_6_5,
sounds.b_1_5,sounds.b_2_5,sounds.b_4_5,sounds.b_5_5,sounds.b_6_5,
sounds.c_1_5,sounds.c_2_5,sounds.c_4_5,sounds.c_5_5,sounds.c_6_5,
sounds.d_1_5,sounds.d_2_5,sounds.d_4_5,sounds.d_5_5,sounds.d_6_5,
sounds.e_1_5,sounds.e_2_5,sounds.e_4_5,sounds.e_5_5,sounds.e_6_5,]

def draw():
    place = 0
    for valeur in range(25):
        do_diese.append(Actor('do_diese_1'))
    screen.fill((254,254,254))
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
    for valeur2 in range(25):
        if do_diese[valeur2].collidepoint(pos):
            notes_diese[valeur2].play()
            musics = 1
            break
    if musics == 0:
        for valeur in range(35):
            if do0[valeur].collidepoint(pos):
                notes[valeur].play()
toucheEncoreEnfonce = []

placement = 2
def on_key_down(key):
    global placement
    do_touche_num = [key.K_1,key.K_2,key.K_3,key.K_4,key.K_5]
    do_touche = [key.S,key.D,key.F,key.G,key.H,key.J,key.K]
    global toucheEncoreEnfonce
    for valeur in range(5):
        if keyboard[do_touche_num[valeur]]:
            placement = valeur
            break
    for valeur in range(7):
        if keyboard[do_touche[valeur]] and detectKey(do_touche[valeur]):
            print(do_touche[valeur])
            notes[valeur + placement * 7].play()
            break
    toucheEncoreEnfonce.append(key)

def on_key_up(key):
    global toucheEncoreEnfonce
    toucheEncoreEnfonce.remove(key)

def detectKey(value):
    global toucheEncoreEnfonce
    if (toucheEncoreEnfonce == []):
        return True
    else:
        for elt in toucheEncoreEnfonce:
            if(elt == value):
                return False
        return True



