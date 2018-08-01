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
                print('Your health is %d! It\'s your turn to attack!' % (hero_health))
                time.sleep(1)
                enemy -= hero_damage
                if enemy > 1:
                    print('Your enemy has %d health!' % enemy)
                    time.sleep(1)
                elif hero_health < 1:
                    print('YOU DIED')
                    break
                else:
                    try:
                        enemy_list.remove(enemy_list[i])
                        print('You killed it! There is %d left!' % (len(enemy_list)))
                        break
                    except IndexError:
                        print('You killed them all! Good job!')
                        break  
                
        



'''hero_dict = {'Health': 20, 'Damage': 5}
enemy_dict = {'Health': 5, 'Damage': 3}
minion_fight(hero_dict, enemy_dict, 3)'''
