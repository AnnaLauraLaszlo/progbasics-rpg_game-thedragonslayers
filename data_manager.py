import csv


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def write_user_dictionary_to_cvs(file_name, dictionary):
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        for key, value in dictionary.items():
            writer.writerow([key, value])


def get_user_dictionary_from_cvs(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        user_data_dict = dict(reader)
    return user_data_dict


def write_event_text_to_csv(file_name, text):
    with open(file_name,'a') as file:
        for line in text:
            file.write(line)