from settings import *
import pygame as pg
import math

class RayCasting:
    def __init__(self, game):
        self.game = game  
        self.ray_casting_result = []  # Armazena resultados dos cálculos
        self.objects_to_render = []  # Lista de objetos para renderizar
        self.textures = self.game.object_renderer.wall_textures  

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            # Ajusta a coluna da textura baseada na altura projetada
            if proj_height < ALTURA:
                # Caso normal: parede mais baixa que a tela
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                # Caso onde a parede é mais alta que a tela
                texture_height = TEXTURE_SIZE * ALTURA / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 
                    HALF_TEXTURE_SIZE - texture_height // 2, 
                    SCALE, texture_height)
                wall_column = pg.transform.scale(wall_column, (SCALE, ALTURA))
                wall_pos = (ray * SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.pos  # Posição do jogador
        x_map, y_map = self.game.player.map_pos  # Posição no mapa

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001  # Ângulo inicial
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Intersecção com linhas horizontais
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.mapa.world_map:
                    texture_hor = self.game.mapa.world_map[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Intersecção com linhas verticais
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.mapa.world_map:
                    texture_vert = self.game.mapa.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # Escolhe a intersecção mais próxima
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # Correção de distorção "olho de peixe"
            depth *= math.cos(self.game.player.angle - ray_angle)

            #desenhar raios de luz
            # pg.draw.line(self.game.tela, "yellow", (100 * ox, 100 * oy), (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)
            
            # Calcula a altura projetada
            proj_height = SCREEN_DIST / (depth + 0.0001)

            #desenhar paredes
            # color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            # pg.draw.rect(self.game.tela, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            # Armazena resultados para renderização
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            ray_angle += DELTA_ANGLE  # Avança para o próximo raio

    def update(self):
        self.ray_cast()  # Calcula todos os raios
        self.get_objects_to_render()  # Prepara objetos para renderização