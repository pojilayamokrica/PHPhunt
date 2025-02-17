import pygame
import random as r

pygame.init()

class PHP(pygame.sprite.Sprite):
    def __init__(self, configs, args):
        super().__init__()
        self.screen_width, self.screen_height = args[1], args[2]
        self.image = configs['image']
        self.rect = self.image.get_rect()
        self.rect.x = r.randint(200, self.screen_width - 200)
        self.rect.y = self.screen_height - self.rect.height - 1
        self.speed = {'start': (configs['speed x'], configs['speed y']),
                      'current': [configs['speed x'] * round(r.uniform(-1, 1), 1), -configs['speed y']]}
        self.score = configs['score']
        self.alive = True
        self.new_duck = True
        self.flying_away = False
        self.is_flying_away = False
        self.is_falling = False
        self.gravity = args[0]
        self.flying_out = False
        self.rect_grass_sprite = args[-1]

    def update(self):
        if self.alive and not self.is_falling:
            if self.rect.bottom > self.rect_grass_sprite.top - 1 and not self.flying_out:
                self.rect.x += round(self.speed['current'][0], 1)
                self.rect.y += round(self.speed['current'][1], 1)
            else:
                self.rect.x += round(self.speed['current'][0], 1)
                self.rect.y += round(self.speed['current'][1], 1)

                if not self.flying_away:
                    if self.rect.left < 0 or self.rect.right > self.screen_width:
                        self.speed['current'][0], self.speed['current'][1] = (
                        self.speed['start'][0], self.speed['start'][1] *
                        ((self.speed['current'][1] >= 0) - (self.speed['current'][1] < 0)))
                        self.speed['current'][0] *= round((r.uniform(-1.0, -0.1) * (self.rect.right > self.screen_width) +
                                                           (r.uniform(0.1, 1.0) * (self.rect.left < 0))), 1)
                    if self.rect.top < 0 or self.rect.bottom > self.rect_grass_sprite.top:
                        self.speed['current'][0], self.speed['current'][1] = (self.speed['start'][0] *
                                                                              ((self.speed['current'][0] >= 0)
                                                                               - (self.speed['current'][0] < 0)),
                                                                              self.speed['start'][1])
                        self.speed['current'][1] *= round(
                            (r.uniform(-1.0, -0.1) * (self.rect.bottom > self.rect_grass_sprite.top) +
                             (r.uniform(0.1, 1.0) * (self.rect.top < 0))), 1)
                elif (not (-1 * self.rect.width) < self.rect.x < self.screen_width
                      or not (-1 * self.rect.height) < self.rect.y < self.screen_height):
                    self.alive = True
                    self.is_flying_away = True

                self.flying_out = True
        else:
            self.falling_animation()

    def falling_animation(self):
        self.speed['current'][1] += self.gravity
        self.rect.y += round(self.speed['current'][1], 1)
        pygame.transform.rotate(self.image, 15)
        if self.rect.y > self.screen_height:
            self.alive = False
            self.flying_away = False

    def draw(self, screen, new=False):
        self.new_duck = new
        if new:
            self.rect.x = r.randint(self.screen_width // 4, self.screen_width // 2)
            self.rect.y = self.screen_height - (self.rect.height + 10)
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, self.rect)