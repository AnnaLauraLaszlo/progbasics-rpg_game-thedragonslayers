import pygame
import ui
from new_game import new_game
import data_manager

pygame.init()


def show_inventory(game_display, inventory_img, x, y):
    game_display.blit(inventory_img, (x, y))


def show_boss_loot(game_display, boss_loot_img, x, y):
    game_display.blit(boss_loot_img, (x, y))


def show_loot_item(game_display, loot_item_img, x, y):
    game_display.blit(loot_item_img, (x, y))


def show_loot_gold(game_display, font, loot_gold_coins):
    gold = font.render("Looted gold: " + str(loot_gold_coins), True, (250, 215, 0))
    game_display.blit(gold, (795, 298))


def show_message(game_display, font, attribute):
    message = font.render("Would you like to equip this item? It will give you " + attribute, True, (255, 255, 255))
    game_display.blit(message, (20, 450))


def show_yes(game_display, font):
    message = font.render("Yes", True, (255, 255, 255))
    game_display.blit(message, (778, 450))


def show_no(game_display, font):
    message = font.render("No", True, (255, 255, 255))
    game_display.blit(message, (864, 450))


def show_sword(game_display, weapon_img, x, y):
    game_display.blit(weapon_img, (x, y))


def show_chest(game_display, costume_img, x, y):
    game_display.blit(costume_img, (x, y))


def show_health(game_display, font, health_points, item_health):
    health_sum = int(health_points) + int(item_health)
    health = font.render("Health: " + str(health_sum), True, (255, 0, 0))
    game_display.blit(health, (35, 30))


def show_attack(game_display, font, attack_points, item_attack):
    attack_sum = int(attack_points) + int(item_attack)
    attack = font.render("Attack: " + str(attack_sum), True, (0, 255, 0))
    game_display.blit(attack, (35, 65))


def show_gold(game_display, font, gold_coins):
    gold = font.render("Gold: " + str(gold_coins), True, (250, 215, 0))
    game_display.blit(gold, (500, 30))


def show_shop(close_shop, game_display):
    clock = pygame.time.Clock()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    boss_loot_img = pygame.image.load("images/boss_loot.png")
    while not close_shop:
        show_boss_loot(game_display, boss_loot_img, 300, 50)
        ui.draw_button(730, 380, 50, 200, game_display, "BACK TO MENU", 738, 395, blue, red, 6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_shop = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 380 and pygame.mouse.get_pos()[1] < 430 and pygame.mouse.get_pos()[0] > 730 and pygame.mouse.get_pos()[0] < 930:
                close_shop = True

        pygame.display.update()
        clock.tick(60)


def main(game_display, close_inventory):
    pygame.display.set_caption("Dragon's loot")
    clock = pygame.time.Clock()
    user_data_dict = data_manager.get_user_dictionary_from_cvs("./hero.csv")

    inventory_img = pygame.image.load("images/inventory.png")
    weapon_img = pygame.image.load(user_data_dict['Weapon image'])
    costume_img = pygame.image.load(user_data_dict['Costume image'])
    boss_loot_img = pygame.image.load("images/boss_loot.png")
    loot_chest_img = pygame.image.load("images/2nd_chest.png")
    loot_sword_img = pygame.image.load("images/2nd_sword.png")

    font = pygame.font.Font("freesansbold.ttf", 24)
    x = 0
    y = 0
    x_sword = 50
    y_sword = 160
    x_chest = 245
    y_chest = 160
    x_loot = 640
    y_loot = 0
    x_loot_item = 625
    y_loot_item = 10

    display_width = 1000
    display_height = 571
    blue = (0, 0, 255)
    black = (0, 0, 0,)
    white = (255, 255, 255)
    red = (150, 0, 0)
    bright_red = (220, 0, 0)
    green = (0, 150, 0)
    bright_green = (0, 220, 0)

    boss_killed = False
    loot_gold_coins = 30
    attribute = " + 20 Health"

    while not close_inventory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_inventory = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 380 and pygame.mouse.get_pos()[1] < 430 and pygame.mouse.get_pos()[0] > 730 and pygame.mouse.get_pos()[0] < 930:
                close_inventory = True

        ui.draw_button(730, 380, 50, 200, game_display, "BACK TO MENU", 738, 395, blue, red, 6)

        show_inventory(game_display, inventory_img, x, y)
        show_sword(game_display, weapon_img, x_sword, y_sword)
        show_chest(game_display, costume_img, x_chest, y_chest)
        if boss_killed:
            show_boss_loot(game_display, boss_loot_img, x_loot, y_loot)
            show_loot_item(game_display, loot_chest_img, x_loot_item, y_loot_item)
            show_loot_gold(game_display, font, loot_gold_coins)
            show_message(game_display, font, attribute)

            mouse = pygame.mouse.get_pos()
            if 770 + 60 > mouse[0] > 770 and 445 + 30 > mouse[1] > 445:
                pygame.draw.rect(game_display, bright_green, (770, 445, 60, 30))
            else:
                pygame.draw.rect(game_display, green, (770, 445, 60, 30))

            if 850 + 60 > mouse[0] > 850 and 445 + 30 > mouse[1] > 445:
                pygame.draw.rect(game_display, bright_red, (850, 445, 60, 30))
            else:
                pygame.draw.rect(game_display, red, (850, 445, 60, 30))
            show_yes(game_display, font)
            show_no(game_display, font)

        show_health(game_display, font, user_data_dict['Health'], user_data_dict['Costume health'])
        show_attack(game_display, font, user_data_dict['Damage'], user_data_dict['Weapon damage'])
        show_gold(game_display, font, user_data_dict['Gold'])
        pygame.display.update()
        clock.tick(60)
