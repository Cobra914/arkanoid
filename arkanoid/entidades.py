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

    velocidad = 10

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_img = os.path.join('resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_img))

        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-25))

    def update(self):
        # 00 -> 01 -> 02 -> 00...
        self.contador += 1

        if self.contador > 2:
            self.contador = 0    
        self.image = self.imagenes[self.contador]

        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0
        if teclas_pulsadas[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
