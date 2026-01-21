import pygame
from ..mechanics.path import path

class Setting():
    def init(self, x, y, width, height, step, hp, file_name, folder_name):
        self.X= x
        self.Y= y
        self.WIDTH= width
        self.HEIGHT= height
        self.STEP= step
        self.HP= hp
        self.FOLDER_NAME= folder_name
        self.FILE_NAME= file_name
    def load_image(self):
        image_load = pygame.image.load(path(self.FOLDER_NAME, self.FILE_NAME))    
        self.IMAGE = pygame.transform.scale(image_load,(self.WIDTH, self.HEIGHT))
    def blit_sprite(self, surface):
        surface.blit(self.IMAGE, (self.X, self.Y))