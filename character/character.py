import data_manager
import csv


def start_module(file_name):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    print("\nYour Character\n")
    for key in user_data_dict:
        print(key, ': ', user_data_dict[key])
    print('\n')
    user_choise = int(input('~0~ Back to Main Menu '))
    if user_choise == '0':
        pass