import sqlite3
from functions import draw_text
from variables import *


def records_sql():
    con = sqlite3.connect('BD PHPhunt/PHPhunt Records.db')
    cur = con.cursor()
    result = cur.execute('''select * from Records''').fetchall()
    return result


def blit_records(screen):
    global stretches
    records = records_sql()
    for line in records:
        draw_text(f'{line[1]}{stretches[str(line[0])][0]}{line[2]}{stretches[str(line[0])][1]}{line[3]}', font,
                  WHITE, screen, screen_width // 2 - 150, screen_height // 2 + 100 - (50 * line[0]))


def update_records(level, score, amount_php, all_php):
    con = sqlite3.connect('BD PHPhunt/PHPhunt Records.db')
    cur = con.cursor()
    records = cur.execute('''select * from Records''').fetchall()
    for line in records:
        if line[0] == current_level and (int(line[2]) < score or int(line[3].split('/')[0]) < amount_php):
            cur.execute(f"""update Records set score={score}, amount_php='{amount_php}/{all_php}' where id={level}""")
            con.commit()


def delete_records():
    con = sqlite3.connect('BD PHPhunt/PHPhunt Records.db')
    cur = con.cursor()
    for id in range(1, 4):
        cur.execute(f"""update Records set score=0, amount_php='0/10' where id={id}""")
        con.commit()


def stretch_for_records():
    records = records_sql()
    stretches = {}
    for line in records:
        score_stretch = ' ' * (((30 - len(line[2])) // 2) + (4 - len(line[1])))
        amount_php_stretch = ' ' * ((30 - len(line[3])) // 2)
        stretches[str(line[0])] = [score_stretch, amount_php_stretch]
    return stretches


stretches = stretch_for_records()
