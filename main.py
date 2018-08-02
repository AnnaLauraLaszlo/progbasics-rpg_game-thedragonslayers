
import ui
import sys
import pygame as pg
import pygame
from new_game import new_game

def choose():
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        new_game.start_module('hero.csv')
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
    
def main():
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    done = False
    gender = True
    CLASS = True
    name = True

    clock = pygame.time.Clock()

    button_hight = 50
    button_width = 150 

    gender_x_pos = 400
    
    gender_result = ""
    class_result = ""
    name_result = ""

    while not done:
        size = (700, 431)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("dragon.jpeg").convert()
        screen.blit(background_image, [0, 0])
        ui.draw_button(250,150,50,200,screen,"START GAME",270,165,WHITE,RED)
        ui.draw_button(250,250,50,200,screen,"EXIT",320,265,WHITE,RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 300 and pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 450:
                done = True
        
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 200 and pygame.mouse.get_pos()[0] > 250 and pygame.mouse.get_pos()[0] < 450 :
                name = False
                done = True

        pygame.display.flip()
        clock.tick(60)

    while not name:
        pg.init()
        screen = pg.display.set_mode((1000, 571))
        clock = pg.time.Clock()
        color_inactive = (255,255,255) 
        font = pg.font.Font(None, 35)        
        color_active = (255,0,0)
        color = color_inactive
        active = False
        text = ''
        done = False
        input_box = pg.Rect(400, 400, 140, 50)
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                        done = True
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN :
                    if active:
                        if event.key == pg.K_RETURN:
                            active = False
                            done = True
                            name = True
                            gender = False
                            name_result = text
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 470 and pygame.mouse.get_pos()[1] < 520 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 520 :
                    name = True
                    gender = False

            if event.type == pygame.QUIT:
                    name = True

            screen.fill((0, 0, 0))
            txt_surface = font.render(text, True, (255,255,255))
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+10, input_box.y+10))
            pg.draw.rect(screen, color, input_box, 2)
            welcome_text = font.render("Welcome passenger!",True,WHITE)
            screen.blit(welcome_text, [150,100])
            welcome_text = font.render("Prepare yourself for the adventure!",True,WHITE)
            screen.blit(welcome_text, [200,200])
            welcome_text = font.render("But first enter your name pls",True,WHITE)
            screen.blit(welcome_text, [200,300])
            welcome_text = font.render("NAME:",True,WHITE)
            screen.blit(welcome_text, [300,415])

            pg.display.flip()
            clock.tick(60)

        

    while not gender:
        size = (1000, 571)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("forest.jpg").convert()
        screen.blit(background_image, [0, 0])
        font = pygame.font.Font(None, 55)
        start_game = font.render("GENDER:",True,WHITE)
        screen.blit(start_game, [100,250])
        ui.draw_button(gender_x_pos,150,button_hight,button_width,screen,"MALE",435,165,WHITE,RED)
        ui.draw_button(gender_x_pos,250,button_hight,button_width,screen,"FEMALE",430,265,WHITE,RED)
        ui.draw_button(gender_x_pos,350,button_hight,button_width,screen,"OTHER",430,365,WHITE,RED)
        ui.draw_button(10,10,50,100,screen,"EXIT",25,25,WHITE,RED)

        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 60 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 110 :
            gender = True

        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 200 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 550 :
            gender = True
            CLASS = False
            gender_result = "male"

        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 250 and pygame.mouse.get_pos()[1] < 300 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 550 :
            gender = True
            CLASS = False
            gender_result = "female"

        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 400 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 550 :
            gender = True
            CLASS = False
            gender_result = "other"
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gender = True
        
        pygame.display.flip()
        clock.tick(60)
    
    while not CLASS:
        size = (1000, 571)
        screen = pygame.display.set_mode(size)
        background_image = pygame.image.load("forest.jpg").convert()
        screen.blit(background_image, [0, 0])
        font = pygame.font.Font(None, 55)
        start_game = font.render("CLASS:",True,WHITE)
        screen.blit(start_game, [100,250])
        ui.draw_button(gender_x_pos,200,button_hight,button_width,screen,"WARRIOR",415,215,WHITE,RED)
        ui.draw_button(gender_x_pos,300,button_hight,button_width,screen,"MAGE",440,315,WHITE,RED)
        ui.draw_button(10,10,50,100,screen,"EXIT",25,25,WHITE,RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 60 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 110 :
                CLASS = True
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 250 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 550 :
                CLASS = True
                class_result = "warrior"
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 550 :
                CLASS = True
                class_result = "mage"
        pygame.display.flip()
        clock.tick(60)
                  

if __name__ == '__main__':
    main()


