import ui
import common
import data_manager
import csv
import os

def start_module(file_name):
    user_data_dict = data_manager.get_user_dictionary_from_cvs(file_name)
    print("\nWelcome back %s!" %(user_data_dict['Name']))