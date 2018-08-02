import pygame
import ui

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
    message = font.render("Would you like to equip this item? It will give you " + attribute, True, (0, 0, 0))
    game_display.blit(message, (20, 450))


def show_yes(game_display, font):
    message = font.render("Yes", True, (255, 255, 255))
    game_display.blit(message, (778, 450))


def show_no(game_display, font):
    message = font.render("No", True, (255, 255, 255))
    game_display.blit(message, (864, 450))


def show_sword(game_display, sword_img, x, y):
    game_display.blit(sword_img, (x, y))


def show_chest(game_display, chest_img, x, y):
    game_display.blit(chest_img, (x, y))


def show_health(game_display, font, health_points):
    health = font.render("Health: " + str(health_points), True, (255, 0, 0))
    game_display.blit(health, (35, 30))


def show_attack(game_display, font, attack_points):
    attack = font.render("Attack: " + str(attack_points), True, (0, 255, 0))
    game_display.blit(attack, (35, 65))


def show_gold(game_display, font, gold_coins):
    gold = font.render("Gold: " + str(gold_coins), True, (250, 215, 0))
    game_display.blit(gold, (500, 30))


def showing_inventory():
    pygame.display.set_caption("Dragon's loot")
    clock = pygame.time.Clock()

    inventory_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/inventory.png")
    sword_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/1st_blade.png")
    chest_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/1st_chest.png")
    boss_loot_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/boss_loot.png")
    loot_chest_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/2nd_chest.png")
    loot_sword_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/2nd_sword.png")
def main(game_display,close_inventory):
    pygame.display.set_caption("Dragon's loot")
    clock = pygame.time.Clock()

    inventory_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/inventory.png")
    sword_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/1st_blade.png")
    chest_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/1st_chest.png")
    boss_loot_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/boss_loot.png")
    loot_chest_img = pygame.image.load("progbasics-rpg_game-thedragonslayers/images/2nd_chest.png")

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
    boss_killed = True

    loot_gold_coins = 30
    attribute = " + 20 Health"

    #close_inventory = False
    #game_display = pygame.display.set_mode((display_width, display_height))
    while not close_inventory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_inventory = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 380 and pygame.mouse.get_pos()[1] < 430 and pygame.mouse.get_pos()[0] > 730 and pygame.mouse.get_pos()[0] < 930 :
                close_inventory = True

        ui.draw_button(730,380,50,200,game_display,"BACK TO MENU",738,395,blue,red,6)

        #game_display.fill(white)
        show_inventory(game_display, inventory_img, x, y)
        show_sword(game_display, sword_img, x_sword, y_sword)
        show_chest(game_display, chest_img, x_chest, y_chest)
        if boss_killed:
            show_boss_loot(game_display, boss_loot_img, x_loot, y_loot)
            show_loot_item(game_display, loot_chest_img, x_loot_item, y_loot_item)
            show_loot_gold(game_display, font, loot_gold_coins)
            show_message(game_display, font, attribute)

            mouse = pygame.mouse.get_pos()
            print(mouse)
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

        show_health(game_display, font, 35)
        show_attack(game_display, font, 9)
        show_gold(game_display, font, 5)
        pygame.display.update()
        clock.tick(60)
