
import pygame
from config import *
from functions import *
from button import Button
pygame.init()
sc = pygame.display.set_mode((w, h))
f = pygame.font.SysFont('arial', 18)



clock = pygame.time.Clock()
color = black
fl_draw_start = False
sp = ep = None
fl_up_i = False
fl_r = False
fl_down_i = False
regym = Brush()
button1 = Button('Brush',(100, 25))
button2 = Button('Rubber',(100, 75))
button3 = Button('RectangleBrush', (100, 125))
button4 = Button('CircleBrush', (100, 175))
button_color = Button('ColorChoose', (100, 225))
i = 1
op = 0
pygame.mouse.set_visible(False)
sc.fill(white)
exit_flag = False
help_txt(f, sc)
while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_ = None
    button1.update()
    button1.draw(sc)
    button2.update()
    button2.draw(sc)
    button3.update()
    button3.draw(sc)
    button4.update()
    button4.draw(sc)
    button_color.update()
    button_color.draw(sc)
    pygame.draw.line(sc, black, (200, 0), (200, 720))
    pygame.draw.line(sc, black, (1000,0), (1000, 720))
    if button1.callback:
        regym = Brush()
        button1.callback = False
    if button2.callback:
        regym = RubberBrush()
        button2.callback = False
    if button3.callback:
        regym = RectangleBrush()
        button3.callback = False
    if button4.callback:
        regym = CircleBrush()
        button4.callback = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fl_draw_start = True
            sp = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                fl_r = True
            if button_color.callback:
                if event.key == pygame.K_0:
                    color = black
                    button_color.callback = False
                elif event.key == pygame.K_1:
                    color = red
                    button_color.callback = False
                elif event.key == pygame.K_2:
                    color = green
                    button_color.callback = False
                elif event.key == pygame.K_3:
                    color = blue
                    button_color.callback = False
            if event.key == pygame.K_UP:
                fl_up_i = True
            if event.key == pygame.K_DOWN:
                fl_down_i = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                fl_up_i = False
            if event.key == pygame.K_r:
                fl_r = False
        if event.type == pygame.K_DOWN:
            fl_down_i = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            fl_draw_start = False
    if fl_up_i:
        if i < 6:
            i += 0.01
    elif fl_down_i:
        if i > 1:
            i -= 0.01
    if fl_draw_start:
        if  1000 > mouse_pos[0] > 200 and mouse_pos[1] > 0:
            mouse_pos_ = pygame.mouse.get_pos()
            regym.draw(sc, color, mouse_pos, mouse_pos_, i)


    pygame.display.update()
    clock.tick(FPS)

