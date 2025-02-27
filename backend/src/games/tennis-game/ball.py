from sprite import Sprite
import pygame

class Ball(Sprite):
  def __init__(self, x, y, image_path):
    super().__init__(x, y, image_path)
    
  #detemine spawnpoint
  SIZE=[15,15]
  SPEED=6


