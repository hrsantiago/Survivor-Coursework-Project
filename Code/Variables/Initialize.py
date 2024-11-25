from Code.Variables.Variables import *
from Code.Utilities.Utils import *
import pygame

display = pygame.display.set_mode(WIN_RES, pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

BG_entities_gif = import_gif("Assets\\Backgrounds\\Background Entities", (12, 9))
Main_Menu_BG = load("Backgrounds\\Menu_BG.png", WIN_RES)
border = load("Backgrounds\\border.png", REN_RES)

loading_screen_1 = import_gif("Assets\\LoadingScreens\\1", WIN_RES)
loading_screen_2 = import_gif("Assets\\LoadingScreens\\2", WIN_RES)

Buttons = import_gif("Assets\\Misc\\Buttons", None)
Health_bar = load("Misc\\Bars\\health.png")
Stamina_bar = load("Misc\\Bars\\Sprite-0005.png")
Outside_Health_bar = load("Misc\\Bars\\health_bar.png", None, (0, 0, 0))

Player_Running = import_SpriteSheet("Assets\\Entities\\Player\\AnimationSheet_Character.png", 0, 98, 32, 32, 8, (0, 0, 0))
Player_Walking = import_SpriteSheet("Assets\\Entities\\Player\\AnimationSheet_Character.png", 0, 2 + 32 * 2, 32, 32, 4, (0, 0, 0))
Player_Dying = import_SpriteSheet("Assets\\Entities\\Player\\AnimationSheet_Character.png", 0, 2 + 32 * 7, 32, 32, 8, (0, 0, 0))
Player_Idle = import_SpriteSheet("Assets\\Entities\\Player\\AnimationSheet_Character.png", 0, 2 + 32 * 0, 32, 32, 2, (0, 0, 0))
Player_Blinking = import_gif("Assets\\Entities\\Player\\AnimationSheet_Character_Blinking", 0, 2 + 32 * 1, 32, 32, 2)

Enemy_idle = import_gif("Assets\\Entities\\Enemy1", ENEMY_RES)

Main_Border_Image = load("Backgrounds\\Foundation\\043.png", None, (255, 255, 255))
Border_Animation_Images = import_gif("Assets\\Backgrounds\\New_Border")

New_Border_Images = import_SpriteSheet("Assets\\Backgrounds\\output-onlinegiftools.png", 0, 0, 960, 534, 44, (255, 255, 255))
New_Border_Images = re_res(New_Border_Images, REN_RES)

Slash_Effect = import_gif("Assets\\VFX\\Slash", )

Rifle = load("Objects\\Weapons\\rifle.png", None, (0, 0, 0))
Rifle_bullet = load("Objects\\Bullet\\Bullet 1\\Bullet.png", None, (0, 0, 0))

cursor1 = load("Misc\\Mouse\\Mouse3\\Sprite-0002.png", MOUSE_RES)
cursor2 = load("Misc\\Mouse\\Mouse3\\Sprite-0001.png", MOUSE_RES,)
cover = load("Misc\\Cover\\cover.png", None)
