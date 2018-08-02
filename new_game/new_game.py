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
            user_data_dict = choose_preset_hero()
            data_manager.write_user_dictionary_to_cvs(file_name, user_data_dict)
            new_game = False
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


def get_user_name(user_name, user_data_dict):
    user_data_dict['Name'] = user_name
    user_data_dict['Level'] = 1
    return user_data_dict


def get_user_gender(user_gender, user_data_dict):
    user_data_dict['Gender'] = user_gender
    return user_data_dict


def get_user_class(user_data_dict):
    user_class = str(input('It\'s time to pick a class! Would you like to be a mage or a warrior? '))
    user_data_dict['Class'] = user_class

    return user_class


def get_class_stats(user_class, user_data_dict):
    hero_health = 0
    hero_damage = 0
    hero_gold = 10
    weapon_list = ['Basic Rod', 'Basic Sword']
    costume_list = ['Basic Robe', 'Basic Armor']
    if user_class.lower() == 'mage':
        hero_weapon = weapon_list[0]
        hero_costume = costume_list[0]
        hero_health = 20
        hero_damage = 10
        hero_weapon_image = "images/1st_wand.png"
        hero_costume_image = "images/1st_robe.png"
        weapon_damage = 5
        costume_health = 10
    if user_class.lower() == 'warrior':
        hero_weapon = weapon_list[1]
        hero_costume = costume_list[1]
        hero_health = 30
        hero_damage = 6
        hero_weapon_image = "images/1st_blade.png"
        hero_costume_image = "images/1st_chest.png"
        weapon_damage = 4
        costume_health = 20

    user_data_dict['Damage'] = hero_damage
    user_data_dict['Health'] = hero_health
    user_data_dict['Gold'] = hero_gold
    user_data_dict['Weapon'] = hero_weapon
    user_data_dict['Costume'] = hero_costume
    user_data_dict['Weapon image'] = hero_weapon_image
    user_data_dict['Weapon damage'] = weapon_damage
    user_data_dict['Costume image'] = hero_costume_image
    user_data_dict['Costume health'] = costume_health

    return user_data_dict


def choose_preset_hero():
    user_data_dict = {'Name': 'Anna', 'Level': 1, 'Gender': 'female', 'Class': 'mage', 'Damage': 10, 'Health': 20, 'Gold': 10, 'Weapon': 'Magic Rod', 'Costume': 'Star Robe'}
    return user_data_dict


def random_hero():
    pass
