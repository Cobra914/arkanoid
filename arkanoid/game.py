import pygame as pg

from . import ANCHO, ALTO

class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        '''
        Bucle principal
        '''
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            self.pantalla.fill((99, 0, 0))
            pg.display.flip()

        pg.quit()


if __name__ == '__main__':
    print('Arrancamos el juego desde game.py')
    juego = Arkanoid()
    juego.jugar()