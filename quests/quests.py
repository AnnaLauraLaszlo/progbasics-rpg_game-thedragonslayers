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

def quests_main(close_quest,user_data_dict):
    clock = pygame.time.Clock()
    black = (0, 0, 0,)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0,0,255)
    while not close_quest:
        size = (1000, 571)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("images/dangerousforest.jpeg").convert()
        screen.blit(background_image, [0, 0])
        font = pygame.font.Font(None, 35)
        welcome_message = font.render("Choose your adventure %s!" % user_data_dict['Name'] ,True,(255, 255, 255))
        screen.blit(welcome_message, [100,100])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_quest = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 20 and pygame.mouse.get_pos()[1] < 70 and pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 220 :
                close_quest = True
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 250 and pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 500 :
                welcome_message = font.render("It is not available yet!",True,(255, 255, 255))
                screen.blit(welcome_message, [520,215])
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 500 :
                welcome_message = font.render("You have to acquire the Dungeon coin!",True,(255, 255, 255))
                screen.blit(welcome_message, [520,315])
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450 and pygame.mouse.get_pos()[0] > 300 and pygame.mouse.get_pos()[0] < 500 :
                welcome_message = font.render("You have to acquire the Mountine coin!",True,(255, 255, 255))
                screen.blit(welcome_message, [520,415])

        ui.draw_button(300,200,50,200,screen,"Forest quest",325,215,blue,red,6)
        ui.draw_button(300,300,50,200,screen,"Dungeon quest",310,315,blue,red,6)
        ui.draw_button(300,400,50,200,screen,"Mountain quest",310,415,blue,red,6)
        ui.draw_button(20,20,50,200,screen,"BACK TO MENU",28,35,blue,red,6)
        pygame.display.update()
        clock.tick(60)

def dungeon_quest(file_name, user_data_dict):
    if user_data_dict['Special Item'] == 'Magic Amulet':
        print('You may enter the Dungeon!')
    else:
        print('You need the Magic Amulet to enter the dungeon!')


def mountain_quest(file_name, user_level):
    password = 'It\'s the age of the dragons.'
    user_input = input('Enter the password. ')
    if user_input == password:
        print('Climb the mountain!')
        pass
    else:
        print('Sorry, you are wrong.')