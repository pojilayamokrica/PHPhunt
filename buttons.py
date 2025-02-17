import time
from functions import create_list_of_ducks
from records import delete_records
from variables import *
import pygame


pygame.init()

def handle_input():
    x_move = 0
    y_move = 0

    # Чтение значений осей контроллера
    if joysticks:
        x_move += joysticks[0].get_axis(0)  # Ось X (левый стик)
        y_move += joysticks[0].get_axis(1)  # Ось Y (левый стик)

    # Чтение клавиатуры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Стрелка влево
        x_move -= 1
    if keys[pygame.K_RIGHT]:  # Стрелка вправо
        x_move += 1
    if keys[pygame.K_UP]:  # Стрелка вверх
        y_move -= 1
    if keys[pygame.K_DOWN]:  # Стрелка вниз
        y_move += 1
    return x_move, y_move

