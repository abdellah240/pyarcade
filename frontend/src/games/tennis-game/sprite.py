import pygame

class Sprite:
  def __init__(self, x,y, image_path):
       self.image_path = image_path
       self.coordinates= x,y
       self.draw()
  
  def draw(self):
    self.image=pygame.image.load(self.image_path)
    self.rect=self.image.get_rect()
    self.rect.center = self.coordinates  