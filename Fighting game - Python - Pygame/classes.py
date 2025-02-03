import pygame
from pathlib import Path

pygame.mixer.init()

class Buttons:

    def __init__(self) -> None:
       
        self.button_font = pygame.font.Font(None, 100)
        


    def first_button(self):

        """ #This method creates the button Start 
        """

        
        button_name = "START"
        button_surface = self.button_font.render(button_name, True, (255, 0, 0))
   

        return button_surface


    def second_button(self):

        """ #This method creates the button Exit 
        """

        
        button_name = "EXIT"
        button_surface = self.button_font.render(button_name, True, (255, 255, 255))
   

        return button_surface
    

    
    def white_first_button(self):
        """ #this method creates a white button 
        """



        button_name = "START"
        button_surface = self.button_font.render(button_name, True, (255, 255, 255))
   

        return button_surface

        
    def red_second_button(self):

        """ #this method creates a red button 
        """

        button_name = "EXIT"
        button_surface = self.button_font.render(button_name, True, (255, 0, 0))
   

        return button_surface
    
    
    def game_over_text(self):
        
        """ #This method is designed to display the GAME OVER announcement 
        """

        ending_text = "GAME OVER"
        font = pygame.font.Font(None, 190)  

        ending_text_surface = font.render(ending_text, True, (255, 255, 255))  

        return ending_text_surface

    def game_over_x(self):
        return 260

    def game_over_y(self):
        return 360
    

    def load_music(self):

        """ #This method is designed to load music in the game 
        """

        music_path_finder = Path(__file__).resolve()
    

        music_actual_path = music_path_finder.parent / "marioforeversong.mp3"

        return music_actual_path







def fighting_area():

    """ #this function is designed to create the background where the fight should unfold 
    """
    
    current_background = Path(__file__).resolve()

    background_path = current_background.parent / "FightingRoom.jpg"

    background_image = pygame.image.load(str(background_path))
    fighting_stage = pygame.Surface(background_image.get_size())


    fighting_stage.blit(background_image, (0, 0))

    return fighting_stage 




