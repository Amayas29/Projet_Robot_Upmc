import pygame as py  

def get_rect(width, height, color, bg):
    surface = py.Surface((width, height))
    surface.set_colorkey(bg)
    surface.fill(color)
    surface.fill((255, 0, 0), rect=py.Rect(0, height-10, width, 10))
    return surface

def rotate(surface, angle):
    old_center = surface.get_rect().center
    new_surface = py.transform.rotate(surface, angle)
    rect = new_surface.get_rect()   
    rect.center = old_center 
    return new_surface