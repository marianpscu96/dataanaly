from pathlib import Path
import pygame
from pygame import mixer
from classes import Buttons, fighting_area
from fighter_class import Fighter, Enemy


pygame.init()


screen_dimensions = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Fighting Game")
clock = pygame.time.Clock()


buttons = Buttons()
my_fighter = Fighter()
my_enemy = Enemy()

pygame.mixer.init()
mixer.music.load(buttons.load_music())
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


start_button_state = True
exit_button_state = False
to_display_buttons = True

switch_to_fighting = False
fighting_stage_state = None
fighting_zone = fighting_area()

running = True

storage_first_button = None
storage_second_button = None



while running:
    
    if not switch_to_fighting:
        
        screen_dimensions.fill((0, 0, 255))  # this is to add the menu screen
    else:
        if fighting_stage_state is None:
            fighting_zone = fighting_area()
        screen_dimensions.blit(fighting_zone, (0, 0))
        to_display_buttons = False 

    if to_display_buttons:
        if exit_button_state:
            storage_first_button = buttons.white_first_button()
            storage_second_button = buttons.red_second_button()
        else:
            storage_first_button = buttons.first_button()
            storage_second_button = buttons.second_button()

        screen_dimensions.blit(storage_first_button, (500, 200))
        screen_dimensions.blit(storage_second_button, (525, 300))
    else:
        storage_first_button = None
        storage_second_button = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                exit_button_state = True
            if event.key == pygame.K_UP:
                exit_button_state = False

    my_keys = pygame.key.get_pressed()
    if my_keys[pygame.K_RETURN] and exit_button_state:
        running = False
    elif my_keys[pygame.K_RETURN] and not exit_button_state:
        switch_to_fighting = True
        to_display_buttons = False


    if switch_to_fighting:

        
        
        
        screen_dimensions.blit(my_fighter.deplete_health(), (my_fighter.health_text_x(), my_fighter.health_text_y()))


        fighter_surface = my_fighter.loading_fighter()
        enemy_surface = my_enemy.load_enemy()
        # my_keys = pygame.key.get_pressed()
        # if my_keys[pygame.K_4]:
        screen_dimensions.blit(enemy_surface, (my_enemy.enemy_x_pos, my_enemy.enemy_y_pos))

        screen_dimensions.blit(fighter_surface, (my_fighter.get_x(), my_fighter.get_y()))
        my_fighter.fighter_movement()
        my_fighter.set_boundary()

        

        my_fighter.bullet_movement()
        my_fighter.bullet_auto_move()

        if my_fighter.bullet_on_move:
            bullet_surface = my_fighter.load_bullet()
            screen_dimensions.blit(bullet_surface, (my_fighter.bullet_x_pos, my_fighter.bullet_y_pos))
            my_fighter.detect_collision()
        else:
            bullet_surface = my_fighter.load_bullet()
            screen_dimensions.blit(bullet_surface, (my_fighter.x_pos, my_fighter.bullet_y_pos))
        
        my_fighter.detect_collision()
        
        if my_fighter.enemy_total_health <= 0:
            screen_dimensions.blit(buttons.game_over_text(), (buttons.game_over_x(), buttons.game_over_y()))
            pygame.time.wait(500)
        


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
pygame.mixer.quit()
