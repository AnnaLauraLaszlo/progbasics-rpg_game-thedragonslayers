

def print_menu(title, list_options, exit_message):
    print(title)
    for i in range(len(list_options)):
        print("\t" + "~" + str(i+1) + "~ " + list_options[i])
    print("\t" + "~0~ " + exit_message)
    
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        inputs.append(input("  " + label))
    return inputs

def print_error_message(message):
    print('Error: ' + message)