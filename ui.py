import pygame
import sys

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

def draw_button (start_x,start_y,high,width,screen,button_name,name_pos_x,name_pos_y,first_color,second_color):
        pygame.draw.rect(screen,first_color,[start_x,start_y,width,high],3)
        font = pygame.font.Font(None, 35)
        start_game = font.render(button_name,True,(255, 255, 255))
        screen.blit(start_game, [name_pos_x,name_pos_y])
        if pygame.mouse.get_pos()[1] > start_y and pygame.mouse.get_pos()[1] < (start_y + high) and pygame.mouse.get_pos()[0] > start_x and pygame.mouse.get_pos()[0] < (start_x+width) :
            pygame.draw.rect(screen,second_color,[start_x,start_y,width,high],3)

"""def main_menu(done,name,first_color,second_color):
    while not done:
        size = (700, 431)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("dragon.jpeg").convert()
        screen.blit(background_image, [0, 0])
        draw_button(250,150,50,200,screen,"START GAME",270,165,first_color,second_color)
        draw_button(250,250,50,200,screen,"EXIT",320,265,first_color,second_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 300 and pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 450:
                done = True
        
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 200 and pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 450 :
                name = False
                done = True

        pygame.display.flip()
    return done, name"""

    
        