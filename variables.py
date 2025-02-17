import pygame
import sys


pygame.init()

screen_width = 800
screen_height = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

screen = pygame.display.set_mode((screen_width, screen_height))

try:
    records_background = pygame.image.load('backgrounds/records.png').convert()
    duck_php_elephant = pygame.image.load('sprites/elephant.png').convert()
    duck_php_elephant.set_colorkey(duck_php_elephant.get_at((0, 0)))
    duck_php_light = pygame.image.load("sprites/php light.jpg").convert()  # Загрузите изображение утки
    duck_php_strong = pygame.image.load('sprites/php hard.png').convert()
    duck_php_strong.set_colorkey(duck_php_strong.get_at((0, 0)))
    background_image = pygame.image.load("backgrounds/background.jpg").convert()  # Загрузите фоновое изображение
    grass_sprite = pygame.image.load('sprites/grass.png').convert()
    grass_sprite.set_colorkey(grass_sprite.get_at((0, 0)))
    kowlad_image = pygame.image.load("sprites/kowlad.png").convert_alpha()
except pygame.error:
    print("Ошибка загрузки изображений. Убедитесь, что файлы существуют и путь к ним указан верно.")
    pygame.quit()
    sys.exit()


levels = {
    'Easy': {'duck_php_light': 7,
             'duck_php_strong': 3,
             'duck_php_elephant': 0},
    'Medium': {'duck_php_light': 5,
               'duck_php_strong': 4,
               'duck_php_elephant': 1},
    'Hard': {'duck_php_light': 4,
             'duck_php_strong': 3,
             'duck_php_elephant': 3}
}

ducks_config = {'duck_php_light': {'image': duck_php_light,
                                   'speed x': 3,
                                   'speed y': 3,
                                   'score': 500},
                'duck_php_strong': {'image': duck_php_strong,
                                    'speed x': 4,
                                    'speed y': 4,
                                    'score': 1000},
                'duck_php_elephant': {'image': duck_php_elephant,
                                      'speed x': 5,
                                      'speed y': 5,
                                      'score': 1500}
                }

new_duck = True
rect_grass_sprite = grass_sprite.get_rect()
rect_grass_sprite.inflate_ip(0, -1100)

GRAVITY = 2
shoot = None
game_state = "menu"

ducks = []
score = 0  # Счетчик очков
amount_shots = 3
font = pygame.font.Font(None, 36)
cur_duck = None
rect_background_sprite = grass_sprite.get_rect()
init_in_main = True
current_level = 1
score_for_duck_position = None
speed_y_score = 0
