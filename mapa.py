import pygame as pg

_ = False

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
        self.mini_mapa = mini_mapa
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_mapa):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.tela, "darkgrey", (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]