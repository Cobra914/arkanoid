import pygame as pg

from . import ANCHO, ALTO
from .escenas import MejoresJugadores, Partida, Portada

class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        records = MejoresJugadores(self.pantalla)

        self.escenas = [
            portada,
            partida,
            records,
        ]


    def jugar(self):
        '''
        Bucle principal
        '''
        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()


if __name__ == '__main__':
    print('Arrancamos el juego desde game.py')
    juego = Arkanoid()
    juego.jugar()