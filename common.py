import ui
import data_manager
import csv
import os
import random
from random import randint
import time


def minion_fight(user_dict, enemy_dict, number_of_enemies):
    hero_health = int(user_dict['Health'])
    hero_damage = int(random.randint((int(user_dict['Damage'])-2), int(user_dict['Damage']) +2))
    enemy_health = int(enemy_dict['Health'])
    enemy_damage = int(random.randint((int(enemy_dict['Damage'])-2), int(enemy_dict['Damage']) +2))
    enemy_list = [enemy_health] * number_of_enemies
    for i in range(len(enemy_list)):
        for enemy in enemy_list:
            while hero_health > 0:
                hero_health -= enemy_damage
                if hero_health < 1:
                    return hero_health
                print('Your health is %d! It\'s your turn to attack!' % (hero_health))
                time.sleep(1)
                enemy -= hero_damage
                if enemy > 1:
                    print('Your enemy has %d health!' % enemy)
                    time.sleep(1)
                else:
                    try:
                        enemy_list.remove(enemy_list[i])
                        print('You killed a %s! There is %d left!' % (enemy_dict['Name'], len(enemy_list)))
                        break
                    except IndexError:
                        print('You killed them all! Good job!')
                        return hero_health
                

def get_weapon(file_name):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    weapon_loot_list = ['Fire Sword', 'Great Sythe']
    hero_loot_weapon = weapon_loot_list[random.randint(0, (len(weapon_loot_list)-1))]
    title = "\nYou have found a %s! Would you like to change it to your default weapon?" % hero_loot_weapon
    list_options = ['Yes, I want the new and op weapon!', 'Nah, I\'m not a filthy casual.']
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == '1':
        return hero_loot_weapon
    else:
        return user_data_dict['Weapon']


def get_costume(file_name):
    costume_loot_list = ['Ice Cloak', 'Dragon Armor']
    hero_costume = costume_loot_list[(random.randint(0, len(weapon_loot_list)))]
    return hero_costume


def game_over(file_name):
    print('YOU DIED')
    print('and')
    print('You\'ve also lost all progress, please start a new game.')
    empty_dictionary = {}
    return empty_dictionary
    


'''hero_dict = {'Health': 2, 'Damage': 20}
enemy_dict = {'Health': 5, 'Damage': 3}
minion_fight(hero_dict, enemy_dict, 10)
get_weapon('hero.csv')'''

#get_weapon('hero.csv')