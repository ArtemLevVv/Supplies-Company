from .settings import Setting
import pygame

class Player(Setting):
    def __init__(self, x=500, y=500, width=90, height=180, step=10, hp=100, file_name='player.png', folder_name='player'):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.STEP = step
        self.HP = hp
        self.FILE_NAME = file_name
        self.FOLDER_NAME = folder_name


    def move_forward(self):
        self.Y -= self.STEP
    def move_backward(self):
        self.Y += self.STEP
    def move_right(self):
        self.X -= self.STEP
    def move_left(self):
        self.X += self.STEP
        
    def movement(self, keys):
        if keys[pygame.K_w]:
            self.move_forward()
        if keys[pygame.K_s]:
            self.move_backward()
        if keys[pygame.K_d]:
            self.move_left()
        if keys[pygame.K_a]:
            self.move_right()
    