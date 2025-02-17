from Crosshair import *
from indicators import *
from Kowlad import *
from buttons import *
from records import *
from functions import *
from variables import *
import pygame
import sys
import time


pygame.init()

pygame.display.set_caption("PHP Hunt")

# Частота обновления экрана
clock = pygame.time.Clock()
FPS = 60

try:
    pygame.mixer.music.load('music pygame/barabariki.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Ошибка загрузки звуков. Убедитесь, что файлы существуют и путь к ним указан верно.")
    pygame.quit()
    sys.exit()

surf_width = 60
surf_height = 60
crosshair_surf = pygame.Surface((surf_width, surf_height))
crosshair_surf.fill(WHITE)
crosshair_surf.set_colorkey(WHITE)
pygame.draw.circle(crosshair_surf, RED, (surf_width // 2, surf_height // 2), radius=25, width=3)
pygame.draw.circle(crosshair_surf, RED, (surf_width // 2, surf_height // 2), radius=6)
pygame.draw.line(crosshair_surf, RED, (0, surf_height // 2), (surf_width, surf_height // 2), width=3)
pygame.draw.line(crosshair_surf, RED, (surf_width // 2, 0), (surf_width // 2, surf_height), width=3)

set_start_pos_crosshair = False
start_pos_crosshair = (screen_width // 2 - surf_width, screen_height // 2 - surf_height)

# Таймер
start_time = time.time()
time_limit = 10

crosshair = Crosshair(crosshair_surf)
indicators = Duck_indicators(screen_width, screen_height)
kowlad = Kowlad_is_true_PHP_programmer(kowlad_image, screen_height)

def eventByPressedKey():
    global game_state, start_time, current_time, running, current_level, shoot, amount_shots
    global set_start_pos_crosshair, ducks, init_in_main
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN and game_state == 'menu':
            if event.key == pygame.K_SPACE:
                game_state = "playing"
                start_time = time.time()  # Сброс таймера
                set_start_pos_crosshair = True
                break
            if event.key == pygame.K_r:
                game_state = "records"
                break
            if event.key == pygame.K_l:
                game_state = "level_select"
                set_start_pos_crosshair = True
                break

        if event.type == pygame.KEYDOWN and game_state == 'level_select':
            if event.key == pygame.K_1:
                current_level = 1
                ducks = create_list_of_ducks(levels['Easy'], ducks_config,
                                             [GRAVITY, screen_width, screen_height, rect_grass_sprite], level=current_level)
                game_state = "playing"
                start_time = time.time()  # Сброс таймера
                break
            elif event.key == pygame.K_2:
                current_level = 2
                ducks = create_list_of_ducks(levels['Medium'], ducks_config,
                                             [GRAVITY, screen_width, screen_height, rect_grass_sprite], level=current_level)
                game_state = "playing"
                start_time = time.time()  # Сброс таймера
                break
            elif event.key == pygame.K_3:
                current_level = 3
                ducks = create_list_of_ducks(levels['Hard'], ducks_config,
                                             [GRAVITY, screen_width, screen_height, rect_grass_sprite], level=current_level)
                game_state = "playing"
                start_time = time.time()  # Сброс таймера
                break
            elif event.key == pygame.K_SPACE:
                game_state = "playing"
                start_time = time.time()  # Сброс таймера
                break
                # Пауза по нажатию клавиши ESC

        if event.type == pygame.KEYDOWN and game_state == "paused":
            if event.key == pygame.K_m:
                game_state = 'menu'
                init_in_main = True
                break
            if event.key == pygame.K_SPACE:
                game_state = "playing"
                break
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 3:
                game_state = 'playing'
                break

        if event.type == pygame.KEYDOWN and game_state == "game_over":
            if event.key == pygame.K_SPACE:
                game_state = "menu"
                init_in_main = True
                break
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 3:
                game_state = "menu"
                break

        if event.type == pygame.KEYDOWN and game_state == 'playing':
            if event.key == pygame.K_p:
                game_state = "paused"
                break
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:  # Кнопка В на геймпаде
                game_state = "paused"
                break

        if event.type == pygame.JOYBUTTONDOWN and game_state == 'playing':
            if event.button == 0:  # Кнопка A на геймпаде
                shoot = True
                break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Клавиша Space для стрельбы
                shoot = True
                break

        if event.type == pygame.KEYDOWN and game_state == 'records':
            if event.key == pygame.K_m:
                game_state = 'menu'
                init_in_main = True
                break
            if event.key == pygame.K_d:
                delete_records()
                break

if __name__ == '__main__':
    running = True
    while running:
        if game_state == 'records':
            screen.blit(records_background, (0, 0))
        else:
            screen.blit(background_image, (0, 0))

        if game_state == "menu":
            if init_in_main:
                score = 0
                cur_duck = None
                ducks = create_list_of_ducks(levels['Easy'], ducks_config,
                                             [GRAVITY, screen_width, screen_height, rect_grass_sprite], level=current_level)
                start_time = time.time()  # Сброс таймера
                new_duck = True
                indicators.__init__(screen_width, screen_height)
                delay_before_game_over_screen = 3
                init_in_main = False
            # Главное меню
            draw_text("PHP hunt", pygame.font.Font(None, 72), BLACK, screen, screen_width // 2 - 100, screen_height // 2 - 300)
            draw_text("Press L to select level", font, BLACK, screen, screen_width // 2 - 100, screen_height // 2 - 200)
            draw_text("Press SPACE to start", font, BLACK, screen, screen_width // 2 - 95, screen_height // 2 - 150)
            draw_text("Press R to see your records", font, BLACK, screen, screen_width // 2 - 120, screen_height // 2 - 100)

        eventByPressedKey()

        if game_state == "level_select":
            # Меню выбора уровня
            draw_text("Select Level", font, BLACK, screen, screen_width // 2 - 100, screen_height // 2 - 100)
            draw_text("1 - Easy, 2 - Medium, 3 - Hard", font, BLACK, screen, screen_width // 2 - 200,
                      screen_height // 2 - 50)

        if game_state == "playing":
            # Обработка ввода
            x_move, y_move = handle_input()
            # Обновление уток
            for duck in ducks:
                if duck.alive and new_duck and not duck.is_flying_away:
                    amount_shots = 3
                    indicators.update(ducks)
                    cur_duck = duck
                    cur_duck.update()
                    cur_duck.draw(screen, new_duck)
                    new_duck = False
                    shoot = False
                    kowlad.__init__(kowlad_image, screen_height)
                    break
                elif cur_duck.alive and not new_duck and not cur_duck.is_flying_away:
                    cur_duck.update()
                    cur_duck.draw(screen)
                    break
                elif kowlad.end_animate or cur_duck.is_flying_away:
                    continue
                else:
                    break

            kowlad.draw(screen)

            screen.blit(grass_sprite, (0, 0))

            # Обновление прицела
            if set_start_pos_crosshair:
                crosshair.draw(screen, start_pos_crosshair)
                set_start_pos_crosshair = False
            else:
                crosshair.draw(screen)

            crosshair.update(x_move, y_move)

            indicators.draw(screen)

            # Проверка попадания
            if shoot and amount_shots > 0:
                if cur_duck.alive and cur_duck.rect.colliderect(crosshair.rect):
                    cur_duck.is_falling = True
                    score_for_duck_position = (cur_duck.rect.x, cur_duck.rect.y)
                    score += cur_duck.score
                    amount_shots -= 1
                    shoot = False
                else:
                    amount_shots -= 1
                    shoot = False
                    # if amount_shots < 0:
                    #     amount_shots = 0

            if cur_duck.is_falling:
                speed_y_score -= 0.1
                draw_text(f'{cur_duck.score}', pygame.font.Font(None, 24), WHITE, screen,
                          score_for_duck_position[0], score_for_duck_position[1] + speed_y_score, visible=150)
            else:
                speed_y_score = 0

            # Отображение счета и жизней
            draw_text(f"Score: {'0' * (6 - len(str(score))) + str(score)}", font, BLACK,
                      screen, screen_width - 250, screen_height - 30)
            draw_text(f"Shots: {amount_shots}", font, RED, screen, 50, screen_height - 30)

            # Отображение таймера
            current_time = time.time()
            time_left = max(0, time_limit - int(current_time - start_time))

            if cur_duck.alive:
                if time_left % 2 == 0:
                    indicators.shimmer(ducks.index(cur_duck), True)
                else:
                    indicators.shimmer(ducks.index(cur_duck), False)
            else:
                indicators.update(ducks)

            if time_left <= 0 and cur_duck.alive or amount_shots == 0:
                cur_duck.flying_away = True
                if not cur_duck.is_flying_away and cur_duck.alive and not cur_duck.is_falling:
                    draw_text('Fly away!', font, WHITE, screen, screen_width - 450, screen_height - 400, visible=150)
                if cur_duck.alive and cur_duck.is_flying_away:
                    new_duck = True
                    start_time = time.time()

            if not cur_duck.alive:
                kowlad.animate()
                if kowlad.end_animate:
                    new_duck = True
                    start_time = time.time()

            if (not cur_duck.alive and kowlad.end_animate) or cur_duck.is_flying_away:
                if all((not duck.alive or duck.is_flying_away) for duck in ducks):
                    indicators.update(ducks)
                    game_state = "game_over"

        if game_state == "paused":
            start_time = time.time()
            draw_text("Paused", font, BLACK, screen, screen_width // 2 - 50, screen_height // 2 - 50)
            draw_text("Press SPACE to resume", font, BLACK, screen, screen_width // 2 - 150, screen_height // 2)
            draw_text("Press M to return to the menu", font, BLACK, screen, screen_width // 2 - 150,
                      screen_height // 2 + 50)

        if game_state == "game_over":
            update_records(current_level, score, sum(indicators.indicators_lighting), len(ducks))
            draw_text("Game Over", font, BLACK, screen, screen_width // 2 - 100, screen_height // 2 - 100)
            draw_text(f"Final Score: {score}", font, BLACK, screen, screen_width // 2 - 130, screen_height // 2 - 50)
            draw_text(f"PHP was shot: {sum(indicators.indicators_lighting)}/{len(ducks)}", font, BLACK, screen,
                      screen_width // 2 - 130, screen_height // 2)
            draw_text("Press SPACE to return to menu", font, BLACK, screen, screen_width // 2 - 200,
                      screen_height // 2 + 50)

        if game_state == 'records':
            blit_records(screen)
            draw_text("Press D to delete your records", font, BLACK, screen, screen_width // 2 - 150,
                      screen_height // 2 + 200)
            draw_text("Press M to return to the menu", font, BLACK, screen, screen_width // 2 - 150,
                      screen_height // 2 + 250)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()