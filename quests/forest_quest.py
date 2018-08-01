import ui
import common
import data_manager
import csv
import os
import random
from random import randint


def start_module(file_name, user_data_dict):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    title = ('Blabla Your job is to get to the forest witch, kill her and get the magic amulet! \n You see a crossroad.')
    list_options = ['Go left!', 'Onwards!', 'Go right!']
    exit_message = "Back to the tavern!"
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs([""], "")
    option = inputs[0]
    if option == '1':
        wolf_event(file_name, user_data_dict)
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '0':
        pass
    else:
        raise KeyError('There is no such option.')

def wolf_event(file_name, user_data_dict):
    forest_enemy_1 = {'Name': 'Wolf', 'Health': 5, 'Damage': 3}
    print('Oh No! You are surrounded by a pack of wolfes! You have to fight!')
    user_data_dict['Health'] = common.minion_fight(user_data_dict, forest_enemy_1, 3)
    data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)

