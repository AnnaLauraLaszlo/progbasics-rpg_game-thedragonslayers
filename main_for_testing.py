
import ui
import sys
import pygame
from new_game import new_game
from quests import quests
from resume import resume
from character import character


def choose():
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        new_game.start_module('hero.csv')
        quests.start_module('hero.csv')
    elif option == "2":
        resume.start_module('hero.csv')
        quests.start_module('hero.csv')
    elif option == "3":
        store.start_module()
    elif option == "4":
        inventory.start_module()
    elif option == "5":
        character.start_module('hero.csv')
    elif option == "6":
        options.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["\033[1;32;48mNew Game",
               "Resume",
               "Store",
               "Inventory",
               "Your Character",
               "Options"]

    ui.print_menu("Main Menu", options, "Exit Game")


def main():
    pygame.init()
    pygame.display.set_caption("The Dragonslayers")
    screen = pygame.display.set_mode((700,600))
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    running = True
    while running:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()

