import ui
import common
import data_manager
import csv
import os
import random
from random import randint


def start_module(file_name, user_data_dict):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    title = ('Your job is to get to the forest witch, kill her and get the magic amulet! \n You see a crossroad.')
    list_options = ['Go left!', 'Onwards!', 'Go right!']
    exit_message = 'Back to the tavern!'
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs([""], "")
    option = inputs[0]
    if option == '1':
        wolf_event(file_name, user_data_dict)
    elif option == '2':
        giant_event(file_name, user_data_dict)
    elif option == '3':
        forest_witch_event(file_name, user_data_dict)
    elif option == '0':
        pass
    else:
        raise KeyError('There is no such option.')
        

def wolf_event(file_name, user_data_dict):
    forest_enemy_1 = {'Name': 'Wolf', 'Health': 5, 'Damage': 3}
    print('Oh No! You are surrounded by a pack of wolfes! You have to fight!')
    data_manager.write_event_text_to_csv('wolf_event.csv', 'Oh No! You are surrounded by a pack of wolfes! You have to fight!')
    user_data_dict['Health'] = common.minion_fight(user_data_dict, forest_enemy_1, 3)
    if user_data_dict['Health'] > 0:
        user_data_dict['Weapon'] = common.get_weapon(file_name)
    else:
        user_data_dict = common.game_over(file_name)
    data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)


def giant_event(file_name, user_data_dict):
    forest_enemy_2 = {'Name': 'Giant', 'Health': 20, 'Damage': 5}
    title = ('You see a giant on the middle of the road. What do you do?')
    list_options = ['Fight the beast!', 'Try to sneak past it!']
    exit_message = 'I\'m scared, let\'s go back to the tavern!'
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs(["Enter a number!"], "")
    option = inputs[0]
    if option == '1':
        user_data_dict['Health'] = common.minion_fight(user_data_dict, forest_enemy_2, 1)
        if user_data_dict['Health'] > 0:
            user_data_dict['Costume'] = common.get_costume(file_name)
        else:
            user_data_dict = common.game_over(file_name)
    elif option == '2':
        pass
    elif option == '0':
        pass
    else:
        raise KeyError('There is no such option.')

    data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)


def forest_witch_event(file_name, user_data_dict):
    forest_enemy_3 = {'Name': 'Forest Witch', 'Health': 20, 'Damage': 3}
    print('You have found the Forest Witch! Kill her to get the amulet!')
    user_data_dict['Health'] = common.minion_fight(user_data_dict, forest_enemy_3, 1)
    user_data_dict['Gold'] = int(user_data_dict['Gold'])
    if user_data_dict['Health'] > 0:
        user_data_dict['Special Item'] = common.get_special_loot()
        user_data_dict['Gold'] += 100
        print('You defeated the Forest Witch, Congratulations!\nYour reward is a Magic Amulet and 100 Gold!\nUse it visely!')
        print('You now have %d gold!' % user_data_dict['Gold'])
    else:
        user_data_dict = common.game_over(file_name)
    data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)

    
