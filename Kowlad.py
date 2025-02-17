import pygame


pygame.init()

class Kowlad_is_true_PHP_programmer(pygame.sprite.Sprite):
    def __init__(self, kowlad_image, screen_height):
        super().__init__()
        self.image = kowlad_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.start_pos = (-self.rect.width, screen_height - (self.rect.height + 30))
        self.speed_x = 2
        self.start_animate = True
        self.end_animate = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animate(self):
        if self.start_animate:
            self.rect.x += self.speed_x
            if self.rect.x > 80:
                self.start_animate = False
        elif self.rect.x > self.start_pos[0]:
            self.rect.x -= self.speed_x
        if self.rect.x <= self.start_pos[0] and not self.start_animate:
            self.end_animate = True