import ui
import common
import data_manager
import csv
import os
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