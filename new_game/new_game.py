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
    new_game = True
    while new_game:
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            get_class_stats(create_hero())
        elif option == '2':
            choose_preset_hero()
        elif option == '3':
            random_hero()
        elif option == '0':
            break
        else:
            raise KeyError("There is no such option.")


def create_hero():
    user_name = input('What is your name wanderer? ')
    user_gender = str(input('Now choose your gender (male, female or other): '))
    if user_gender.lower() == 'male':
        print('Hello sir')
    elif user_gender.lower() == 'female':
        print('Hello miss')
    elif user_gender.lower() == 'other':
        print('Hello you')
    else:
        raise KeyError('There is no such option. Yet.')
        choose_new_game()
    user_class = str(input('It\'s time to pick a class! Would you like to be a mage or a warrior? '))

    return user_class

def choose_preset_hero():
    pass


def random_hero():
    pass

def get_class_stats(user_class):
    hero_health = 0
    hero_damage = 0
    weapon_list = ['magic rod', 'great axe']
    if user_class.lower() == 'mage':
        hero_weapon = weapon_list[0]
        hero_health = 10
        hero_damage = 5
    if user_class.lower() == 'warrior':
        hero_weapon = weapon_list[1]
        hero_health = 5
        hero_damage = 10
    
    return hero_damage, hero_health, hero_weapon

