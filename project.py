
import pygame
from config import *
from functions import *
from pygame.sprite import Group
from button import Button

pygame.init()

screen = pygame.display.set_mode((w, h))
f = pygame.font.SysFont('arial', 16)
f1 = pygame.font.SysFont('arial', 30)

color = (red, green, blue)
red = 0
green = 0
blue = 0
color_ = 8
color = black
i = 2

figure_draw_start = (0, 0)
fl_draw_start = False
sp = ep = None
fl_up_i = False
fl_r = False
fl_down_i = False

title_font = pygame.font.SysFont('Arial', 32)
under_title_font = pygame.font.SysFont('Arial', 24)
title_surface = title_font.render('Whiteboard', True, 'black')
under_title_surface = under_title_font.render('1.0', True, 'gray')

regym = Brush()

buttons_group = Group()

def button1_callback():
    global regym
    regym = Brush()
def button2_callback():
    global regym
    regym = RubberBrush()
def button3_callback():
    global regym
    regym = RectangleBrush()
def button4_callback():
    global regym
    regym = CircleBrush()

def button_color_red_up_callback():
    global red, color_
    red = abs((red + color_) % 256)

def button_color_red_down_callback():
    global red, color_
    red = abs((red - color_) % 256)

def button_color_green_up_callback():
    global green, color_
    green = abs((green + color_) % 256)

def button_color_green_down_callback():
    global green, color_
    green = abs((green - color_) % 256)

def button_color_blue_up_callback():
    global blue, color_
    blue = abs((blue + color_) % 256)

def button_color_blue_down_callback():
    global blue, color_
    blue = abs((blue - color_) % 256)

def button_size_up_callback():
    global i
    if  i < 200:
        i += 1
def button_size_down_callabck():
    global i
    if i > 2:
        i -= 1

button1 = Button('Brush',(101, 100), width=180, callback=button1_callback)
button2 = Button('Rubber',(101, 150), width=180, callback=button2_callback)
button3 = Button('RectangleBrush', (101, 200), width=180, callback=button3_callback)
button4 = Button('CircleBrush', (101, 250), width=180, callback=button4_callback)
buttons_group.add(button1, button2, button3, button4)

button_color_red_up = Button('+red', (49, 320), button_color_red_up_callback, 85, 40)
button_color_green_up = Button('+green', (49, 370), button_color_green_up_callback, 85, 40)
button_color_blue_up = Button('+blue', (49, 420), button_color_blue_up_callback, 85, 40)
button_color_red_down = Button('-red', (150, 320), button_color_red_down_callback, 85, 40)
button_color_green_down = Button('-green', (150, 370), button_color_green_down_callback, 85, 40)
button_color_blue_down = Button('-blue', (150, 420), button_color_blue_down_callback, 85, 40)
buttons_group.add(button_color_red_up, button_color_green_up, button_color_blue_up)
buttons_group.add(button_color_red_down, button_color_green_down, button_color_blue_down)

button_size_up = Button('+size', (49, 600), button_size_up_callback, 85, 40)
button_size_down = Button('-size', (150, 600), button_size_down_callabck, 85, 40)
buttons_group.add(button_size_up, button_size_down)

pygame.mouse.set_visible(False)

screen.fill(white)
screen.blit(title_surface, (15, 15))
screen.blit(under_title_surface, (80, 45))
pygame.draw.line(screen, black, (200, 0), (200, 720))
pygame.draw.line(screen, black, (1001,0), (1001, 720))
help_txt(f, screen)

current_screen = screen.copy()

draw_field = pygame.Surface((800, 720))
draw_field.fill('white')
draw_field_rect = pygame.Rect((201, 0), (800, 720))

exit_flag = False
clock = pygame.time.Clock()

mouse_pos = (400, 400)
mouse_pos_ = None

while True:
    mouse_pos_ = mouse_pos
    real_mouse_pos = pygame.mouse.get_pos()
    mouse_pos = (real_mouse_pos[0] - 201, real_mouse_pos[1])

    screen.blit(current_screen, (0, 0))
    screen.blit(draw_field, (201, 0))

    buttons_group.update()
    buttons_group.draw(screen)
    pygame.draw.rect(screen, color, (10, 450, 180, 100))

    # Рисуем курсор
    if draw_field_rect.collidepoint(real_mouse_pos):
        pygame.draw.circle(screen, 'white', real_mouse_pos, radius=i+1)
        pygame.draw.circle(screen, 'red', real_mouse_pos, radius=i)
    else:
        pygame.draw.circle(screen, 'white', real_mouse_pos, radius=6)
        pygame.draw.circle(screen, 'black', real_mouse_pos, radius=5)

    color = (red, green, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fl_draw_start = True
            figure_draw_start = real_mouse_pos
            sp = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            fl_draw_start = False




    if fl_draw_start:
        if isinstance(regym, (Brush, RubberBrush)):
            print(mouse_pos, mouse_pos_)
            regym.draw(draw_field, color, mouse_pos, mouse_pos_, i)
        if isinstance(regym, (RectangleBrush, CircleBrush)):
            regym.draw(screen, color, real_mouse_pos, figure_draw_start, i)
    elif figure_draw_start is not None:
        if isinstance(regym, (RectangleBrush, CircleBrush)):
            figure_draw_start = (figure_draw_start[0] - 201, figure_draw_start[1])
            regym.draw(draw_field, color, mouse_pos, figure_draw_start, i)
        figure_draw_start = None

    pygame.display.update()
    clock.tick(FPS)




