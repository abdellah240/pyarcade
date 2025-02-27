from sprite import Sprite
import pygame
class Player(Sprite):
  def __init__(self, x, y, image_path):
    super().__init__(x, y, image_path)
        
  SIZE=[40,55]
  SPEED=7
  