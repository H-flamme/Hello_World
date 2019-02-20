WIDTH = 735
HEIGHT = 99

touche = Actor('do_diese_1')
touche.pos = 10,10

def draw():
    screen.fill((254,254,254))
    touche.draw()

def on_mouse_down(pos):
    if touche.collidepoint(pos):
        print("touché")
        sounds.eep.play()