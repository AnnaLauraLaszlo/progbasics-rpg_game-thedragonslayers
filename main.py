
import ui
import sys
from new_game import new_game


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        new_game.start_module()
    elif option == "2":
        resume.start_module()
    elif option == "3":
        store.start_module()
    elif option == "4":
        inventory.start_module()
    elif option == "5":
        level_up.start_module()
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
               "Level Up",
               "Options"]

    ui.print_menu("Main Menu", options, "Exit Game")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
