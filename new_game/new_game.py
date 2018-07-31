import ui
import common
import data_manager


def start_module():
    title = "\nNew Game"
    list_options = ["Create Hero", "Choose Preset Hero", "Random Hero"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    choose_new_game()


def choose_new_game():
    while True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            create_hero()
        elif option == '2':
            choose_preset_hero()
        elif option == '3':
            random_hero()
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")


def create_hero():
    pass


def choose_preset_hero():
    pass


def random_hero():
    pass
