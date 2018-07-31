import ui
import common

def start_module():
    title = "\nNew Game"
    list_options = ["Create Character", "Choose Preset Character", "Random Character"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    choose_new_game()

def choose_new_game():
    while True:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
