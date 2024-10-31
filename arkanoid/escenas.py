# estándar
import os

# librerías de terceros
import pygame as pg

# mis dependencias
from . import ALTO, ANCHO


class Escena:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        

    def bucle_principal(self):
        '''
        Este método debe ser implementado por todas y cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida
        del bucle de la escena,
        '''
        print('Método vacío bucle principal de Escena')


class Portada(Escena):
    
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((99, 0, 0))

            # pintar el logotipo
            ancho, alto = self.logo.get_size()
            pos_x = (ANCHO - ancho) / 2
            pos_y = (ALTO - alto) / 2
            self.pantalla.blit(self.logo, (pos_x, pos_y))

            pg.display.flip()


class Partida(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
    
    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((0, 99, 0))
            pg.display.flip()


class MejoresJugadores(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
    
    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((0, 0, 99))
            pg.display.flip()