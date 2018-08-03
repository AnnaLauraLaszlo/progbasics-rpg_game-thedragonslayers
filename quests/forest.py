import ui
import common
import data_manager
import csv
import os
import quests
from inventory import inventory
import random
from random import randint
import pygame
import time


def forest_main(game_display, close_forest_quest, user_data_dict):
    clock = pygame.time.Clock()
    black = (0, 0, 0,)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    while not close_forest_quest:
        size = (1000, 571)
        show_hero = pygame.image.load("images/hero.png")
        show_enemy = pygame.image.load("images/wolf.png")
        background_image = pygame.image.load("images/forest_quest.jpg").convert()
        game_display.blit(background_image, (0, 0))
        font = pygame.font.Font(None, 35)
        boss_killed = False
        if not boss_killed:
            message = font.render("You arrived to the forest...", True, (255, 255, 255))
            game_display.blit(message, (350, 450))
            message = font.render("Oh No! You are surrounded by a pack of wolfes!", True, (255, 255, 255))
            game_display.blit(message, (290, 490))
            game_display.blit(show_hero, (400, 40))
            game_display.blit(show_enemy, (270, 200))
            pygame.time.wait(600)
        # boss_killed = True
        if boss_killed:
            close_inventory = False
            inventory.main(game_display, close_inventory, boss_killed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_forest_quest = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 550 and pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 220:
                close_forest_quest = True

        ui.draw_button(20, 500, 50, 200, game_display, "BACK TO MENU", 28, 515, blue, red, 6)
        pygame.display.update()
        clock.tick(60)
