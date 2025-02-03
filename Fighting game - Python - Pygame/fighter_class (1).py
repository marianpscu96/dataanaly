from pathlib import Path
import pygame


class Enemy:
    def __init__(self) -> None:
        self.enemy_x_pos = 900
        self.enemy_y_pos = 200


    def load_enemy(self):
        """This method is designed to load the enemy image 
        """

        enemy_path_finder = Path(__file__).resolve()
    

        enemy_image_path = enemy_path_finder.parent / "enemy.png"

        enemy_loaded_image = pygame.image.load(enemy_image_path)

        return enemy_loaded_image



class Fighter:
    def __init__(self) -> None:
        self.x_pos = 100
        self.y_pos = 200
        self.bullet_x_pos = 0
        self.bullet_y_pos = 490
        self.bullet_on_move = False
        self.enemy_total_health = 5

    
    def get_x(self):

        """ this method is designed to provide the x position of the fighter 
        """
        
        fighter_x_pos = self.x_pos
        
        return fighter_x_pos
    

    def get_y(self):

        """ #this method is designed to provide the y position of the fighter 
        """

        fighter_y_pos = self.y_pos
        
        return fighter_y_pos
    

    def loading_fighter(self):

        """ #This method is designed to load the fighter image 
        """

        fighter_path_finder = Path(__file__).resolve()
    

        fighter_image_path = fighter_path_finder.parent / "fighter.png"

        fighter_loaded_image = pygame.image.load(fighter_image_path)
        


        return fighter_loaded_image


    def fighter_movement(self):

        """ #This method is designed to assign keys to the fighter 
        """    

        my_keys = pygame.key.get_pressed()
        if my_keys[pygame.K_RIGHT]:
            self.x_pos += 10

        elif my_keys[pygame.K_LEFT]:
            self.x_pos -= 10


    def set_boundary(self):

        """ #This method is designed to keep the fighter within the screen boundaries 
        """

        if self.x_pos < 0:
            self.x_pos = 0
        
        elif self.x_pos > 1048:
            self.x_pos = 1048

        return self.x_pos
    
    def load_bullet(self):

        """ #This method is designed to load the bullet image 
        """

        bullet_path_finder = Path(__file__).resolve()
    

        bullet_image_path = bullet_path_finder.parent / "Kunai.png"

        bullet_loaded_image = pygame.image.load(bullet_image_path)

    
        return bullet_loaded_image
    
    def bullet_movement(self):
         
         """ #This method is designed to launch a bullet after pressing SPACE 
         """

         my_keys = pygame.key.get_pressed()

         if my_keys[pygame.K_SPACE]:
            
                self.bullet_on_move = True

    
    def bullet_auto_move(self):

        """ #This method is designed to increment the x value of the bullet, and also reset it to the initial position 
        """

        if self.bullet_on_move:
            self.bullet_x_pos +=20

        if self.bullet_x_pos == 980 or self.bullet_x_pos > 1280:
            self.bullet_x_pos = self.get_x()
            self.bullet_on_move = False

    def detect_collision(self):

        """ #This method is designed to check if the bullet hits its target 
        """

        collided = None
        
        if self.bullet_x_pos == 900:
            collided = True

        return collided
    

    def deplete_health(self):

        """ #This method is designed to print and update the health on the screen 
        """
        

        if self.detect_collision():
            self.enemy_total_health -=1

        health_bar = "Health" +":" + str(self.enemy_total_health)
        font = pygame.font.Font(None, 52)  

        health_text_surface = font.render(health_bar, True, (255, 255, 255))  

        return health_text_surface


    def health_text_x(self):
        """ #This method is designed to set the x parameter of the Health update 
        """
        return 1040
    
    def health_text_y(self):
        """ #This method is designed to set the y parameter of the Health update 
        """
        return 20








    

    


        