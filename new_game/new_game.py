import ui
import common
import data_manager
import csv
import os


def start_module(file_name):
    title = "\nNew Game"
    list_options = ["Create Hero", "Choose Preset Hero", "Random Hero"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    user_data_dict = {}
    choose_new_game(file_name, user_data_dict)


def choose_new_game(file_name, user_data_dict):

    new_game = True
    while new_game:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            create_hero(user_data_dict)
            data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)
            new_game = False
        elif option == '2':
            choose_preset_hero()
        elif option == '3':
            random_hero()
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")


def create_hero(user_data_dict):
        get_user_name(user_data_dict)
        get_user_gender(user_data_dict)
        get_class_stats(get_user_class(user_data_dict), user_data_dict)
        print(user_data_dict)

def get_user_name(user_data_dict):
    user_name = input('What is your name wanderer? ')
    user_data_dict['Name'] = user_name
    user_data_dict['Level'] = 1
    
    return user_data_dict


def get_user_gender(user_data_dict):
    user_gender = str(input('Now choose your gender (male, female or other): '))
    if user_gender.lower() == 'male':
        print('Hello sir!')
    elif user_gender.lower() == 'female':
        print('Hello miss!')
    elif user_gender.lower() == 'other':
        print('Hello you!')
    else:
        raise KeyError('There is no such option. Yet.')
    user_data_dict['Gender'] = user_gender

    return user_data_dict

def get_user_class(user_data_dict):
    user_class = str(input('It\'s time to pick a class! Would you like to be a mage or a warrior? '))
    user_data_dict['Class'] = user_class

    return user_class


def get_class_stats(user_class, user_data_dict):
    hero_health = 0
    hero_damage = 0
    weapon_list = ['magic rod', 'great axe']
    if user_class.lower() == 'mage':
        hero_weapon = weapon_list[0]
        hero_health = 20
        hero_damage = 7
    if user_class.lower() == 'warrior':
        hero_weapon = weapon_list[1]
        hero_health = 25
        hero_damage = 5
    
    user_data_dict['Damage'] = hero_damage
    user_data_dict['Health'] = hero_health
    user_data_dict['Weapon'] = hero_weapon

    return user_data_dict




def choose_preset_hero():
    pass


def random_hero():
    pass