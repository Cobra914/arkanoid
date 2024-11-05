import os
from random import randint

import pygame as pg

from . import ALTO, ANCHO, VEL_MAX, VEL_MIN_Y



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


class Ladrillo(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        ruta_verde = os.path.join('resources', 'images', 'greenTile.png')
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()
        

    def update(self):
        pass


class Pelota(pg.sprite.Sprite):

    def __init__(self, raqueta):
        super().__init__()

        ruta_pelota = os.path.join('resources', 'images', 'ball1.png')

        self.image = pg.image.load(ruta_pelota)
        self.raqueta = raqueta
        self.init_velocidades()

    def update(self, partida_empezada):
        if not partida_empezada:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            if self.rect.left < 0 or self.rect.right > ANCHO:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top < 0:
                self.vel_y = -self.vel_y

            if self.rect.top > ALTO:
                self.pierdes()
                self.reset()

            if pg.sprite.collide_mask(self, self.raqueta):
                self.init_velocidades()

    def pierdes(self):
        print('pierdes una vida')

    def reset(self):
        print('La pelota debe volver a su posición inicial')

    def init_velocidades(self):
        self.vel_x = randint(-VEL_MAX, VEL_MAX) 
        self.vel_y = randint(-VEL_MAX, VEL_MIN_Y)
