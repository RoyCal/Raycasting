import pygame as pg

_ = False  # Define um alias para espaços vazios

# Matriz que representa o mapa (1-8: paredes, False: espaços vazios)
mini_mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, 5, _, _, _, _, 2, _, _, _, 1],
    [1, _, _, _, _, _, 5, _, _, _, _, 2, _, _, _, 1],
    [1, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Mapa:
    def __init__(self, game):
        self.game = game  
        self.mini_mapa = mini_mapa  # Armazena a matriz do mapa
        self.world_map = {}  # Dicionário para armazenar paredes
        self.get_map()  # Processa o mapa

    def get_map(self):
        # Converte a matriz 2D em um dicionário eficiente:
        for j, row in enumerate(self.mini_mapa):  
            for i, value in enumerate(row):
                if value:  
                    self.world_map[(i, j)] = value  
    
    def draw(self):
        # Desenha o mapa em 2D (para debug):
        [pg.draw.rect(self.game.tela, "darkgrey", 
                      (pos[0] * 100, pos[1] * 100, 100, 100), 2) 
         for pos in self.world_map]  # List comprehension para eficiência