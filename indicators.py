import pygame


pygame.init()

height_indicators = 40
width_indicators = 200

class Duck_indicators(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.surf = pygame.Surface((width_indicators, height_indicators))
        self.rect = self.surf.get_rect()
        self.position = ((screen_width - self.rect.width) // 2, screen_height - (self.rect.height))
        self.rect.x, self.rect.y = self.position
        self.stretch = 0
        self.indicators_lighting = []
        self.start_pos_indicators = (0, height_indicators // 2)
        pygame.draw.rect(self.surf, pygame.Color('grey10'), (0, 0, width_indicators, height_indicators), 0)

    def update(self, list_ducks):
        self.stretch = width_indicators // (len(list_ducks) + 1)
        self.indicators_lighting = [(not duck.alive and not duck.is_flying_away) for duck in list_ducks]

    def draw(self, screen):
        for index in range(len(self.indicators_lighting)):
            if self.indicators_lighting[index]:
                pygame.draw.circle(self.surf, pygame.color.Color('greenyellow'),
                                   (self.start_pos_indicators[0] + self.stretch * (index + 1),
                                    self.start_pos_indicators[1]),
                                   radius=5, width=5)
            else:
                pygame.draw.circle(self.surf, pygame.color.Color('grey80'),
                                   (self.start_pos_indicators[0] + self.stretch * (index + 1),
                                    self.start_pos_indicators[1]),
                                   radius=5, width=5)
        screen.blit(self.surf, self.rect)

    def shimmer(self, cur_duck, changed):
        if changed:
            self.indicators_lighting[cur_duck] = changed
        else:
            self.indicators_lighting[cur_duck] = changed