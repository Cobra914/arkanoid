import os
from random import randint

import pygame as pg

from . import ALTO, ANCHO, VEL_MAX, VEL_MIN_Y, TAM_LETRA_MARCADOR, COLOR_MARCADOR



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

    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2
    IMG_LADRILLO = ['greenTile.png', 'redTile.png', 'redTileBreak.png']

    def __init__(self, color=VERDE, puntuacion_ladrillo=0):
        super().__init__()

        self.tipo = color
        self.puntuacion_ladrillo = puntuacion_ladrillo
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join('resources', 'images', img)
            self.imagenes.append(pg.image.load(ruta))

    
        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()
        

    def update(self):
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
        else:
            self.kill()
            return self.puntuacion_ladrillo
        self.image = self.imagenes[self.tipo]
        return 0


class Pelota(pg.sprite.Sprite):

    def __init__(self, raqueta):
        super().__init__()

        ruta_pelota = os.path.join('resources', 'images', 'ball1.png')

        self.image = pg.image.load(ruta_pelota)
        self.raqueta = raqueta
        self.init_velocidades()
        self.he_perdido = False

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
                self.he_perdido = True

            if pg.sprite.collide_mask(self, self.raqueta):
                self.init_velocidades()
                

    def init_velocidades(self):
        self.vel_x = randint(-VEL_MAX, VEL_MAX) 
        self.vel_y = randint(-VEL_MAX, VEL_MIN_Y)


class ContadorVidas:

    def __init__(self, vidas_iniciales, jugador):
        self.vidas = []
        for vida in range(vidas_iniciales):
            vida = Vida(jugador)
            self.vidas.append(vida)

    def perder_vida(self):
        self.vidas.pop()
        print('has perdido una vida, te quedan:', len(self.vidas))
        return len(self.vidas) == 0

    def pintar(self, pantalla):
        contador = 0
        for vida in self.vidas:
            vida.pintar_vida(pantalla, contador)
            contador =+ 1



class Vida:
    
    def __init__(self, jugador):
        self.image = jugador.image
        self.rect = self.image.get_rect()
        self.ancho = self.rect.width
        self.alto = self.rect.height

    def pintar_vida(self, pantalla, contador):
        margen_izq = 10
        margen_inf = 10
        espacio_entre_jugador = 5
        x = self.ancho * contador + margen_izq + espacio_entre_jugador * contador
        y = ALTO - margen_inf - self.alto
        pantalla.blit(self.image, (x,y))


class Marcador:

    def __init__(self):
        self.preparar_tipografia()
        self.reset()

    def preparar_tipografia(self):
        tipos = pg.font.get_fonts()
        letra = 'luminari'
        if letra not in tipos:
            letra = pg.font.get_default_font()
        self.tipo_letra = pg.font.SysFont(letra, TAM_LETRA_MARCADOR, True)

    def reset(self):
        self.puntuacion = 0

    def pintame(self, pantalla):
        puntuacion = str(self.puntuacion)
        img_texto = self.tipo_letra.render(puntuacion, True, COLOR_MARCADOR)
        alto_img_texto = img_texto.get_height()
        x = ANCHO - ANCHO
        y = ALTO - (alto_img_texto * 2)
        pantalla.blit(img_texto, (x, y))

    def incrementar(self, puntuacion_ladrillo_destruido):
        self.puntuacion = self.puntuacion + puntuacion_ladrillo_destruido