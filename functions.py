import pygame
from config import *


class AbsractBrush:
    def draw(self):
        print( 'Method "draw" not released')
        exit()
class Brush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_, i):
        pygame.draw.line(sc, color, mouse_pos, mouse_pos_, int(i))
        pygame.display.update()
class RubberBrush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_, i):
        pygame.draw.line(sc, white, mouse_pos, mouse_pos_, int(i*15))
        pygame.display.update()
class RectangleBrush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_, i):
        width = 50
        heigth = 50
        pygame.draw.rect(sc, color, (mouse_pos[0], mouse_pos[1], width, heigth), 2)
        pygame.display.update()
class CircleBrush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_ ,i):
        pygame.draw.circle(sc, color, mouse_pos, i*5, 1)
        pygame.display.update()
def help_txt(f, sc):
    help_text = f.render('Помощь', True, black)
    help_text1 = f.render('Для изменения цвета:', True, black)
    help_text2 = f.render('Нажимайте на кнопки:', True, black)
    help_text3 = f.render('red_up, green_up, blue_up', True, black)
    help_text4 = f.render('red_down, green_down, blue_down', True, black)
    help_text5 = f.render('Цвета кодируются в системе RGB', True, black)
#     # # help_text6 = f.render('', True, black)
#     # # help_text7 = f.render('Нажимайте стрелки вверх и вниз', True, black)
#     # # help_text8 = f.render('Изменение размера применимо для', True, black)
#     # # help_text9 = f.render('Brush, Rubber, CircleBrush', True, black)
    sc.blit(help_text, (1050, 20))
    sc.blit(help_text1, (1050, 50))
    sc.blit(help_text2, (1050, 80))
    sc.blit(help_text3, (1050, 110))
    sc.blit(help_text4, (1050, 140))
    sc.blit(help_text5, (1050, 170))
#     # sc.blit(help_text6, (1050, 200))
#     # sc.blit(help_text7, (1050, 230))
