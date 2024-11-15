# estándar
import os

# librerías de terceros
import pygame as pg

# mis dependencias
from . import ALTO, ANCHO, FPS, VIDAS_INICIALES
from .entidades import Ladrillo, Pelota, Raqueta, ContadorVidas, Marcador


class Escena:

    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
        

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

        ruta_letra = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.tipo_letra = pg.font.Font(ruta_letra, 25)

    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True

            self.pantalla.fill((99, 0, 0))

            self.pintar_logo()
            self.pintar_mensaje()

            pg.display.flip()

        return False

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO - ancho) / 2
        pos_y = (ALTO - alto) / 2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = 'Pulsa <ESPACIO> para comenzar la partida'
        img_texto = self.tipo_letra.render(mensaje, True, (255, 255, 255))
        pos_x = (ANCHO - img_texto.get_width()) / 2
        pos_y = 3/4 * ALTO
        self.pantalla.blit(img_texto, (pos_x, pos_y))


class Partida(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta_fondo = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)
        self.contador_vidas = ContadorVidas(VIDAS_INICIALES, self.jugador)
        self.marcador = Marcador()
    
    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False
        self.crear_muro()
        juego_iniciado = False

        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if pg.QUIT == evento.type or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    juego_iniciado = True

            self.pintar_fondo()
            self.muro.draw(self.pantalla)
            
            self.contador_vidas.pintar(self.pantalla)

            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            self.marcador.pintame(self.pantalla)

            self.pelota.update(juego_iniciado)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            if self.pelota.he_perdido:
               salir = self.contador_vidas.perder_vida()
               self.contador_vidas.pintar(self.pantalla)
               juego_iniciado = False
               self.pelota.he_perdido = False

            golpeados = pg.sprite.spritecollide(self.pelota, self.muro, False)


            if len(golpeados) > 0:
                for ladrillo in golpeados:
                    puntuacion_ladrillo = 0
                    puntuacion_ladrillo = ladrillo.update()
                self.marcador.incrementar(puntuacion_ladrillo)
                self.pelota.vel_y = -self.pelota.vel_y

            pg.display.flip()

    def pintar_fondo(self):
        # TODO mejorar como "rellenar" toda la pantalla con el fondo sin usar copio/pego
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0,0))

    def crear_muro(self):
        filas = 2
        columnas = 6 
        margen_superior = 20
        valor_ladrillo_verde = 10
        tipo = None
        ladrillo_puntuacion = 0
        

        for fila in range(filas):
            for col in range(columnas):
                if tipo == Ladrillo.ROJO:
                    tipo = Ladrillo.VERDE
                    ladrillo_puntuacion = (filas - fila) * valor_ladrillo_verde
                else:
                    tipo = Ladrillo.ROJO
                    ladrillo_puntuacion = (filas - fila) * valor_ladrillo_verde * (Ladrillo.ROJO + 1)

                ladrillo = Ladrillo(tipo, ladrillo_puntuacion)
                ancho_muro = ladrillo.rect.width * columnas
                margen_izquierdo = (ANCHO - ancho_muro) / 2
                ladrillo.rect.x = ladrillo.rect.width * col + margen_izquierdo
                ladrillo.rect.y = ladrillo.rect.height * fila + margen_superior
                self.muro.add(ladrillo)



class MejoresJugadores(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
    
    def bucle_principal(self):
        super().bucle_principal()
    
        salir = False

        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                    return True

            self.pantalla.fill((0, 0, 99))
            pg.display.flip()