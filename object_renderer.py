import pygame as pg
from settings import *  

class ObjectRenderer:
    def __init__(self, game):
        self.game = game  
        self.tela = game.tela  # Superfície de renderização
        self.wall_textures = self.load_wall_textures()  # Carrega todas as texturas

    def draw(self):
        self.render_game_objects()  # Encapsula a lógica de renderização

    def render_game_objects(self):
        # Renderiza objetos processados pelo raycasting:
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:  
            self.tela.blit(image, pos)  # Desenha a textura na posição calculada

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        # Carrega e redimensiona uma textura:
        texture = pg.image.load(path).convert_alpha()  
        return pg.transform.scale(texture, res)  # Redimensiona
    
    def load_wall_textures(self):
        # Pré-carrega todas as texturas do jogo:
        return {
            1: self.get_texture('textures/1.png'),
            2: self.get_texture('textures/2.png'),
            3: self.get_texture('textures/3.png'),
            4: self.get_texture('textures/4.png'),
            5: self.get_texture('textures/5.png')
        }