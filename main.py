from arkanoid import ANCHO, ALTO
from arkanoid.game import Arkanoid


if __name__ == '__main__':
    print('Arrancamos el juego desde main.py')
    print(f'La pantalla tiene un tamanyo de ({ANCHO}, {ALTO})')
    juego = Arkanoid()
    juego.jugar()