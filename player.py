from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game  
        self.x, self.y = PLAYER_POS  # Posição inicial 
        self.angle = PLAYER_ANGLE  # Ângulo inicial 

    def movement(self):
        # Pré-calcula seno e cosseno para otimização
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0  # Inicializa deslocamento
        speed = PLAYER_SPEED * self.game.delta_time  # Velocidade ajustada pelo tempo de frame
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        # Movimento para frente/trás (W/S)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        
        # Movimento lateral (A/D) - strafing
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        # Verifica colisão antes de aplicar movimento
        self.check_wall_collision(dx, dy)
        
        # Rotação (setas esquerda/direita)
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau  # Normaliza o ângulo entre 0 e 2π

    def check_wall(self, x, y):
        return (x, y) not in self.game.mapa.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        # pg.draw.line(self.game.tela, "yellow", (self.x * 100, self.y * 100), (self.x * 100 + LARGURA * math.cos(self.angle), self.y * 100 + LARGURA * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.tela, "green", (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)