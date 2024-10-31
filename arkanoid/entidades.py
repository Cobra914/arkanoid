import os

import pygame as pg

from . import ALTO, ANCHO



class Raqueta(pg.sprite.Sprite):
    '''
    1. Es un tipo Sprite (usar herencia)
    2. Se puede mover (método)
    3. Pintar en pantalla (método)
    4. Volver a la posición inicial
    5.......
    '''
    def __init__(self):
        super().__init__()
        ruta_img = os.path.join('resources', 'images', 'electric00.png')
        self.image = pg.image.load(ruta_img)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))


    def pintar(self):
        pass
