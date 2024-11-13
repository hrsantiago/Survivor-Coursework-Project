import pygame

WIN_RES = 1920, 1080
PLAYABLE_AREA = 3840, 2160
REN_RES = 640, 480

MIN_WIN_RES = 1280, 720
MAX_WIN_RES = 2560, 1440

PLAYER_RES = 25, 50
PLAYER_VEL = 200
PLAYER_DAMAGE = 30
PLAYER_HEALTH = 100
PLAYER_STAMINA = 100
PLAYER_ACCELERATION = 600

PLAYER_GUN_DISTANCE = -1
PLAYER_GUN_RES = 20, 20
PLAYER_BULLET_RES = 24, 24
PLAYER_BULLET_DAMAGE = 20
PLAYER_BULLET_LIFETIME = 1000
PLAYER_BULLET_SPEED = 700
PLAYER_BULLET_RATE = 0.1
PLAYER_BULLET_ANIMATION = 15
PLAYER_NAME = "Player"

ENEMY_RES = 48, 54
ENEMY_VEL = 250
ENEMY_DAMAGE = 20
ENEMY_HEALTH = 100
ENEMY_SPAWN_RATE = 5
ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT = 10, 10
ENEMY_BULLET_DAMAGE = 10
ENEMY_BULLET_LIFETIME = 1000
ENEMY_BULLET_SPEED = 700
ENEMY_NAME = "Enemy"

BG_ENTITIES_DENSITY = 30
BG_ENTITIES_RES = 24, 19

BARS_RES = 90, 20
ANIMATION_SPEED = 5
SPATIAL_GRID_SIZE = 100
BG_COLOUR = (22, 22, 24)
GAME_NAME = "Vampire Survivor"
BUTTONS_SIZE = 1.1
FONT = "Assets\\Font\\font2.ttf"
FPS = 240
MOUSE_RES = 25, 25
WINDOW_MAX_OFFSET = 0.3
WINDOW_LERP_SPEED = 0.05

PLAY_BUTTON_NAME = "Play"
PLAY_BUTTON_POS = 300, 500
PLAY_BUTTON_BASE_COLOUR = "black"
PLAY_BUTTON_HOVERING_COLOUR = "blue"

OPTIONS_BUTTON_NAME = "Options"
OPTIONS_BUTTON_POS = 700, 800
OPTIONS_BUTTON_BASE_COLOUR = "black"
OPTIONS_BUTTON_HOVERING_COLOUR = "blue"

QUIT_BUTTON_NAME = "Quit"
QUIT_BUTTON_POS = 500, 700
QUIT_BUTTON_BASE_COLOUR = "black"
QUIT_BUTTON_HOVERING_COLOUR = "blue"

FULLSCREEN_KEY = pygame.K_F11
TOGGLE_FPS_KEY = pygame.K_F12

START_WITH_FPS = True
START_FULLSCREEN = False
