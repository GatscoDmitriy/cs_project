import pygame

from pygame.sprite import Sprite

from config import *

class Button(Sprite):
    width: int
    height: int

    center: tuple

    text: str
    text_surface: pygame.Surface
    callback: callable

    def __init__(self, text, center, callback=None, width=200, height=50) -> None:
        Sprite.__init__(self)

        # Инициализируем переменные
        self.text = text
        self.width = width
        self.height = height
        self.center = center
        self.callback = callback
        self.pressed = False

        # Фон кнопки под цвет фона приложения
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BACKGROUND_COLOR)

        # Рисуем прямоугольник
        pygame.draw.rect(self.image, BUTTON_COLLOR, (0, 0, self.width, self.height))

        # Выставляем положение кнопки
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.center

        # Рисуем текст
        self.font = pygame.font.Font(None, 24)
        self.text_surface = self.font.render(self.text, True, 'white')
        # Вычисляем позицию для текста
        x = (self.width - self.text_surface.get_width()) // 2
        y = (self.height - self.text_surface.get_height()) // 2
        self.text_pos = (x, y)
        self.image.blit(self.text_surface, self.text_pos)

    def update(self):
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(pos) and pressed:
            self.image.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.image, HOVERED_BUTTON_COLOR, (3, 2, self.width - 6, self.height - 4))
            self.image.blit(self.text_surface, self.text_pos)
            self.pressed = True
        elif self.rect.collidepoint(pos):
            self.image.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.image, HOVERED_BUTTON_COLOR, (0, 0, self.width, self.height))
            self.image.blit(self.text_surface, self.text_pos)
            if self.pressed:
                if self.callback != None:
                    self.callback()
                self.pressed = False
        else:
            self.image.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.image, BUTTON_COLLOR, (0, 0, self.width, self.height))
            self.image.blit(self.text_surface, self.text_pos)
            if self.pressed:
                self.pressed = False
    def draw(self, surface):
        surface.blit(self.image, self.rect)
