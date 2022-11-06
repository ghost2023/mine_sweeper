import random
import sys

import pygame

CELL_SIZE = 64;
NO_OF_BOMBS = 12;
CELLS = [] 
HIDDEN:list[list[int]] = []
BOMBS:list[list[int]] =[]
FLAGGED:list[list[int]] = []

pygame.init()
screen = pygame.display.set_mode((640, 640))


def generate_bombs():
    while len(BOMBS) < 12:
        new_pos = [random.randint(0, 9), random.randint(0, 9)]
        if new_pos not in BOMBS:
            BOMBS.append(new_pos)

def render_cells():
    pass

def render_bombs():
    for bomb in BOMBS:
        rec = pygame.Rect(
                bomb[0] * CELL_SIZE,
                bomb[1] * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )

def render_flags():
    pass

is_game_over = False


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coord = [
                    pygame.mouse.get_pos()[0] // CELL_SIZE,
                    pygame.mouse.get_pos()[1] // CELL_SIZE,
                ]
                if(coord in BOMBS):
                    is_game_over = True
            #     user_input(coord)
            # load_background()
            # draw_pieces()
        render_bombs()

        pygame.display.update()

generate_bombs()
main()
