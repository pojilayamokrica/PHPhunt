import random as r
from PHP_class import PHP


def draw_text(text, font, color, surface, x, y, visible=255):
    text_obj = font.render(text, True, color)
    text_obj.set_alpha(visible)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def create_list_of_ducks(amount_ducks, ducks_config, args, level=1):
    amount_php_light = [PHP(ducks_config['duck_php_light'], args) for _ in range(amount_ducks['duck_php_light'])]
    amount_php_strong = [PHP(ducks_config['duck_php_strong'], args) for _ in range(amount_ducks['duck_php_strong'])]
    amount_php_elephant = [PHP(ducks_config['duck_php_elephant'], args) for _ in range(amount_ducks['duck_php_elephant'])]
    ducks_list = amount_php_light + amount_php_strong + amount_php_elephant
    r.shuffle(ducks_list)
    return ducks_list