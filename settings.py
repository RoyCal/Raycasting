import math

RES = LARGURA, ALTURA = 1600, 900  # Resolução da janela
HALF_WIDTH = LARGURA // 2
HALF_HEIGHT = ALTURA // 2
FPS = 0                           # Será definido dinamicamente (valor inicial)

PLAYER_POS = 1.5, 5               # Posição inicial (x, y) em unidades de mapa
PLAYER_ANGLE = 0                  # Ângulo inicial (em radianos)
PLAYER_SPEED = 0.004              # Velocidade de movimento base
PLAYER_ROT_SPEED = 0.002          # Velocidade de rotação
PLAYER_SIZE_SCALE = 60            # Escala para cálculo de colisão

FOV = math.pi / 3                 # Campo de visão (60 graus em radianos)
HALF_FOV = FOV / 2                # Metade do campo de visão
NUM_RAYS = LARGURA // 2           # Número de raios a serem lançados
HALF_NUM_RAYS = NUM_RAYS // 2     # Metade do número de raios
DELTA_ANGLE = FOV / NUM_RAYS      # Ângulo entre raios consecutivos
MAX_DEPTH = 20                    # Distância máxima de renderização

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)    # Distância "virtual" da tela
SCALE = LARGURA // NUM_RAYS                      # Largura de cada coluna de pixels

TEXTURE_SIZE = 256                               # Tamanho padrão das texturas (quadradas)
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2            # Metade do tamanho da textura