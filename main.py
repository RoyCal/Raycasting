import pygame as pg
import sys
from settings import *
from mapa import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pg.init()  # Inicializa o pygame
        self.tela = pg.display.set_mode(RES)  # Cria a janela com resolução definida em settings.py
        self.clock = pg.time.Clock()  # Cria um relógio para controlar FPS
        self.delta_time = 1  # Inicializa variável de tempo entre frames
        self.new_game() 

    def new_game(self):
        # Inicializa todos os sistemas do jogo:
        self.mapa = Mapa(self)  
        self.player = Player(self)  
        self.object_renderer = ObjectRenderer(self)  
        self.raycasting = RayCasting(self)  

    def update(self):
        # Atualiza a lógica do jogo a cada frame:
        self.player.update() 
        self.raycasting.update()
        pg.display.flip()  
        self.delta_time = self.clock.tick(FPS)  # Controla FPS e armazena tempo do frame
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')  # Mostra FPS na janela

    def draw(self):
        # Renderiza o jogo:
        self.tela.fill("black")  # Limpa a tela
        self.object_renderer.draw()  # Renderiza a visão 3D
        # self.mapa.draw()
        # self.player.draw()

    def check_events(self):
        # Verifica eventos de entrada/saída:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()  
                sys.exit()  
    
    def run(self):
        # Loop principal do jogo:
        while True:
            self.check_events()  # Verifica inputs
            self.update()  # Atualiza lógica
            self.draw()  # Renderiza cena

if __name__ == "__main__":
    game = Game()  
    game.run()  