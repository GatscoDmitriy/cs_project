import pygame
from config import *

def get_intermediate_points(mouse_pos, mouse_pos_):
    count = 1000

    x1, y1 = mouse_pos
    x2, y2 = mouse_pos_

    dx = (x2 - x1) / count
    dy = (y2 - y1) / count
    
    a = []
    a.append((x1, y1))
    for i in range(count - 2):
        a.append((a[-1][0] + dx, a[-1][1] + dy))
    a.append(mouse_pos_)
    return a

def left_corner_point(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    upper_left_x = min(x1, x2)
    upper_left_y = min(y1, y2)
    return (upper_left_x, upper_left_y)
    

class AbsractBrush:
    def draw(self):
        print( 'Method "draw" not released')
        exit()

class Brush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_, i):
        for point in get_intermediate_points(mouse_pos, mouse_pos_):
            pygame.draw.circle(sc, color, point, int(i))

class RubberBrush(AbsractBrush):
    def draw(self, sc, color, mouse_pos, mouse_pos_, i):
        for point in get_intermediate_points(mouse_pos, mouse_pos_):
            pygame.draw.circle(sc, white, point, int(i))

class AbstractFigureBrush(AbsractBrush):
    def __init__(self) -> None:

        self.start_point = (0, 0)
        self.end_point = (0, 0)

    def get_transparent_surface(self, size):
        image = pygame.Surface(size, pygame.SRCALPHA, 32)
        image = image.convert_alpha()
        return image
    
class RectangleBrush(AbstractFigureBrush):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self, sc, color, mouse_pos, start_pos, i):
        size = (abs(mouse_pos[0] - start_pos[0]), abs(mouse_pos[1] - start_pos[1]))
        image = self.get_transparent_surface(size)
        rect = pygame.Rect((0, 0), size)
        pygame.draw.rect(image, color, rect, width=i)
        sc.blit(image, left_corner_point(mouse_pos, start_pos))

class CircleBrush(AbstractFigureBrush):
    def __init__(self) -> None:
        super().__init__()

    def draw(self, sc, color, mouse_pos, start_pos, i):
        size = (abs(mouse_pos[0] - start_pos[0]), abs(mouse_pos[1] - start_pos[1]))
        image = self.get_transparent_surface(size)
        rect = pygame.Rect((0, 0), size)
        pygame.draw.ellipse(image, color, rect, i)
        sc.blit(image, left_corner_point(mouse_pos, start_pos))

def help_txt(f, sc):
    help_text = f.render('Помощь', True, black)
    help_text1 = f.render('Для изменения цвета', True, black)
    help_text2 = f.render('нажимайте на кнопки:', True, black)
    help_text3 = f.render('+red и -red', True, black)
    help_text4 = f.render('+green и -green', True, black)
    help_text5 = f.render('+blue и -blue', True, black)
    help_text6 = f.render('Цвета кодируются', True, black)
    help_text7 = f.render('в RGB формате', True, black)
    sc.blit(help_text, (1050, 20))
    sc.blit(help_text1, (1050, 50))
    sc.blit(help_text2, (1050, 80))
    sc.blit(help_text3, (1050, 110))
    sc.blit(help_text4, (1050, 140))
    sc.blit(help_text5, (1050, 170))
    sc.blit(help_text6, (1050, 200))
    sc.blit(help_text7, (1050, 230))
