import ui
import common
import data_manager
import csv
import os
import sys
import pygame as pg
import pygame 
from quests import forest_quest

def start_module(file_name):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    title = ('Welcome to the village tavern, %s! ' % user_data_dict['Name'] )
    list_options = ['Forest quest', 'Dungeon quest', 'Mountain quest']
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    choose_adventure(file_name, user_data_dict)


def choose_adventure(file_name, user_data_dict):
    inputs = ui.get_inputs(["Choose your adventure!\n"], "")
    option = inputs[0]
    if option == '1':
        forest_quest.start_module(file_name, user_data_dict)
    elif option == '2':
        dungeon_quest(file_name, user_data_dict)
    elif option == '3':
        mountain_quest(file_name, user_data_dict)
    elif option == '0':
        pass
    else:
        raise KeyError('There is no such option!')

def quests(close_quest):
    clock = pygame.time.Clock()
    black = (0, 0, 0,)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0,0,255)
    while not close_quest:
        size = (1000, 571)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/dangerousforest.jpeg").convert()
        screen.blit(background_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_quest = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 380 and pygame.mouse.get_pos()[1] < 430 and pygame.mouse.get_pos()[0] > 730 and pygame.mouse.get_pos()[0] < 930 :
                close_quest = True

        ui.draw_button(730,380,50,200,screen,"BACK TO MENU",738,395,blue,red,6)
        pygame.display.update()
        clock.tick(60)

'''def forest_quest(file_name, user_data_dict):
    


def dungeon_quest(file_name, user_level):
    pass


def mountain_quest(file_name, user_level):
    pass'''