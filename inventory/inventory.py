import pygame

pygame.init()


def show_inventory(game_display, inventory_img, x, y):
    game_display.blit(inventory_img, (x, y))


def show_boss_loot(game_display, boss_loot_img, x, y):
    game_display.blit(boss_loot_img, (x, y))


def show_loot_chest(game_display, loot_chest_img, x, y):
    game_display.blit(loot_chest_img, (x, y))


def show_loot_gold(game_display, font, loot_gold_coins):
    gold = font.render("Looted gold: " + str(loot_gold_coins), True, (250, 215, 0))
    game_display.blit(gold, (795, 298))


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


def main():
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
    x_loot_chest = 625
    y_loot_chest = 10

    display_width = 1000
    display_height = 571

    black = (0, 0, 0,)
    white = (255, 255, 255)
    red = (255, 0, 0)

    loot_gold_coins = 30

    close_inventory = False
    game_display = pygame.display.set_mode((display_width, display_height))
    while not close_inventory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_inventory = True

        game_display.fill(white)
        show_inventory(game_display, inventory_img, x, y)
        show_sword(game_display, sword_img, x_sword, y_sword)
        show_chest(game_display, chest_img, x_chest, y_chest)
        show_boss_loot(game_display, boss_loot_img, x_loot, y_loot)
        show_loot_chest(game_display, loot_chest_img, x_loot_chest, y_loot_chest)
        show_loot_gold(game_display, font, loot_gold_coins)
        show_health(game_display, font, 35)
        show_attack(game_display, font, 9)
        show_gold(game_display, font, 5)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


'''if __name__ == '__main__':
    main()'''
