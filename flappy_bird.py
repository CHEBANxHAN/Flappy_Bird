import pygame as pg
from pygame.mixer import music as mg
from random import*
import time
pg.init()
W = 300
H = 500
sc = pg.display.set_mode((W, H), pg.SCALED)
pg.display.set_caption("Flapy Bird")
f1 = pg.font.Font("Data/pix.ttf", 24)
f2 = pg.font.Font("Data/pix.ttf", 24)

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
p = BLACK
FPS = 60
clock = pg.time.Clock()

xb = 125
yb = 200
xs = 300
ys = randint(10, H - 10 - 150)
xt1 = 300
yt1 = 0
score = 0

velY = 1
force = 30
    

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                 yb -= force
                 mg.load("Data/flap.mp3")
                 mg.play(0)

    yb += velY
    xt1 -= 0.5
    xs -= 0.5

    with open("Score.txt") as r:
        hs = r.read()
        r.close()

    if xt1 < xb + 50 < xt1 + 50 and yb < yt1 + ys:
        mg.load("Data/loose.mp3")
        mg.play(0)
        exit()

    if xt1 < xb + 50 < xt1 + 50 and yb > yt1 + ys + 150:
        mg.load("Data/loose.mp3")
        mg.play(0)
        exit()

    if xb + 25 == xs + 25 and ys < yb < ys + 150:
        score += 1

    if xt1 < -50:
        xs = 300
        ys = randint(10, H - 10 - 150)
        xt1 = 300
        yt1 = 0

    if yb + 50 < 0 or yb > H:
        mg.load("Data/loose.mp3")
        mg.play(0)
        exit()

    if score > int(hs):
        w = open("Score.txt", "w")
        w.write(str(score))
        w.close()
        
    sc_text1 = f1.render(f"S:{score}", 1, WHITE, BLACK)
    pos1 = sc_text1.get_rect(center=(50, 20))
    sc_text2 = f2.render(f"H:{hs}", 1, WHITE, BLACK)
    pos2 = sc_text2.get_rect(center=(50, 50))
    sc.fill(BLACK)
    pg.draw.rect(sc, GREEN, (xt1,yt1, 50, 500))
    pg.draw.rect(sc, BLACK, (xs,ys, 50, 150))
    bird = pg.draw.rect(sc, YELLOW, (xb,yb, 50, 50))
    sc.blit(sc_text1, pos1)
    sc.blit(sc_text2, pos2)
    pg.display.update()

    clock.tick(FPS)
