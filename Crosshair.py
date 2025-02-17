from variables import *
import pygame


pygame.init()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, crosshair_surf):
        super().__init__()
        self.surf = crosshair_surf
        self.rect = self.surf.get_rect()
        self.rect.inflate_ip(-30, -30)
        self.speed = 5  # Скорость перемещения прицела
        self.rect_grass_sprite = rect_grass_sprite

    def update(self, x_move, y_move):
        # Обновление позиции прицела
        self.rect.x += x_move * self.speed
        self.rect.y += y_move * self.speed

        # Ограничение движения прицела в пределах экрана
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.rect_grass_sprite.top - self.rect.height * 2))

    def draw(self, screen, position=None):
        if position is not None:
            self.rect.x, self.rect.y = position
            screen.blit(self.surf, self.rect)
        else:
            screen.blit(self.surf, self.rect)