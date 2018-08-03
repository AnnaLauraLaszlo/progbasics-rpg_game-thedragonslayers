import pygame
import sys


def print_menu(title, list_options, exit_message):
    print(title)
    for i in range(len(list_options)):
        print("\t" + "~" + str(i+1) + "~ " + list_options[i])
    print("\t" + "~0~ " + exit_message)


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        inputs.append(input("  " + label))
    return inputs


def print_error_message(message):
    print('Error: ' + message)


def draw_button(start_x, start_y, high, width, screen, button_name, name_pos_x, name_pos_y, first_color, second_color, button_width):
    pygame.draw.rect(screen, first_color, [start_x, start_y, width, high], button_width)
    font = pygame.font.Font(None, 35)
    start_game = font.render(button_name, True, (255, 255, 255))
    screen.blit(start_game, [name_pos_x, name_pos_y])
    if pygame.mouse.get_pos()[1] > start_y and pygame.mouse.get_pos()[1] < (start_y + high) and pygame.mouse.get_pos()[0] > start_x and pygame.mouse.get_pos()[0] < (start_x+width):
        pygame.draw.rect(screen, second_color, [start_x, start_y, width, high], button_width)
