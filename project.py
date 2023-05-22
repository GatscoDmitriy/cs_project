
import pygame
from config import *
from functions import *
from button import Button
pygame.init()
sc = pygame.display.set_mode((w, h))
f = pygame.font.SysFont('arial', 18)
f1 = pygame.font.SysFont('arial', 30)

color = (red, green, blue)
red = 0
green = 0
blue = 0
color_ = 8
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
button_color_red_up = Button('red_up', (45, 320), False, 90, 40)
button_color_green_up = Button('green_up', (45, 370), False, 90, 40)
button_color_blue_up = Button('blue_up', (45, 420), False, 90, 40)
button_color_red_down = Button('red_down', (150, 320), False, 100, 40)
button_color_green_down = Button('green_down', (150, 370), False, 100, 40)
button_color_blue_down = Button('blue_down', (150, 420), False, 100, 40)

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
    button_color_red_up.update()
    button_color_red_up.draw(sc)
    button_color_green_up.update()
    button_color_green_up.draw(sc)
    button_color_blue_up.update()
    button_color_blue_up.draw(sc)
    button_color_red_down.update()
    button_color_red_down.draw(sc)
    button_color_green_down.update()
    button_color_green_down.draw(sc)
    button_color_blue_down.update()
    button_color_blue_down.draw(sc)
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
    if button_color_red_up.callback:
        if red < 256:
            red += color_
            if red >= 256:
                red = 255
        button_color_red_up.callback = False
    if button_color_green_up.callback:
        if  green < 256:
            green += color_
            if green >= 256:
                green = 255
        button_color_green_up.callback = False
    if button_color_blue_up.callback:
        if blue < 256:
            blue += color_
            if blue >= 256:
                blue = 255
        button_color_blue_up.callback = False
    if button_color_red_down.callback:
        if red == 255:
            red -= 7
        elif red != 255:
            if red > 0:
                red -= color_
        button_color_red_down.callback = False
    if button_color_green_down.callback:
        if green == 255:
            green -= 7
        elif green != 255:
            if green > 0:
                green -= color_
        button_color_green_down.callback = False
    if button_color_blue_down.callback:
        if blue == 255:
            blue -= 7
        elif blue != 255:
            if blue > 0:
                blue -= color_
        button_color_blue_down.callback = False

    color = (red, green, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fl_draw_start = True
            sp = event.pos
        elif event.type == pygame.KEYDOWN:

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

    color_text = f1.render(f'color: ({str(color[0])}, {str(color[1])}, {str(color[2])})', False, black)
    sc.blit(color_text, (30, 450))
    pygame.display.update()
    clock.tick(FPS)


