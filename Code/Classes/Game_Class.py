import pygame, time, math
import pandas as pd
from Code.Variables.Variables import *
from Code.Classes.Managers import *
from Code.Utilities.Grid import *
from Code.Display.UI import *
from Code.Classes.Entities import *
from Code.Variables.Initialize import *
from Code.Display.Window import *
from Code.Display.Menu import *
from Code.Classes.Buttons import *
from Code.Display.EventManager import *


class Game:
          def __init__(self):
                    pygame.init()
                    self.display = display
                    self.display_screen = pygame.Surface(REN_RES).convert()
                    self.ui_surface = pygame.Surface((480, 270)).convert()
                    self.ui_surface.set_colorkey((0, 0, 0))
                    self.clock = pygame.time.Clock()

                    self.settings = Settings(self)
                    self.mainmenu = MainMenu(self)
                    self.game_over = GameOver(self)

                    self.event_manager = EventManager(self)
                    self.enemy_manager = EnemyManager(self)
                    self.particle_manager = ParticleManager(self)
                    self.object_manager = ObjectManager(self)
                    self.bullet_manager = BulletManager(self)
                    self.button_manager = ButtonManager(self)
                    self.sound_manager = SoundManager(self)
                    self.BG_entities = BGEntitiesManager(self)

                    self.ui = UI(self)

                    self.window = Window(self, REN_RES, PLAYABLE_AREA_SIZE)
                    self.big_window = PLAYABLE_AREA_SIZE

                    self.player = Player(self, PLAYER_HEALTH, PLAYER_RES, PLAYER_VEL, PLAYER_DAMAGE, self.window.rect.center, PLAYER_NAME, Player_Running)

                    self.running = True
                    self.game_time = 0
                    self.fps = pygame.display.get_current_refresh_rate()
                    self.dt = 0
                    self.changing_settings = False
                    self.immidiate_quit = False
                    self.update_game_variables()

                    self.stats = pd.DataFrame(columns=['Coins', 'Score', 'Enemies Killed'])
                    #new_stat = pd.DataFrame({'Coins': [Coins], 'Score': [score], 'Enemies': [enemies], 'Enemies Killed': [Enemies_Killed]})
                    #self.stats = pd.concat([self.stats, new_stat], ignore_index=True)


          def refresh(self):
                    self.__init__()
                    pygame.display.flip()
                    self.run_game()

          def update_groups(self):
                    if not self.changing_settings:
                              self.enemy_manager.update_enemies()
                              self.particle_manager.update()
                              self.bullet_manager.update()
                              self.game_over.update()
                              self.object_manager.update()
                    self.player.update()
                    self.player.gun.update()
                    self.button_manager.update_buttons()

          def draw_groups(self):
                    self.display_screen.fill(BG_COLOUR)
                    self.BG_entities.draw()
                    self.player.draw()
                    self.player.gun.draw()
                    self.enemy_manager.draw_enemies()
                    self.object_manager.draw()
                    self.bullet_manager.draw()
                    self.particle_manager.draw()
                    self.ui.darken_screen()
                    self.ui.draw_border()
                    self.ui.draw_bars()
                    self.ui.draw_fps()
                    self.ui.draw_time()
                    self.button_manager.draw_buttons()
                    self.display_screen.blit(self.ui_surface)
                    self.display.blit(pygame.transform.scale(self.display_screen, self.display.size))
                    self.ui.display_mouse()
                    self.ui.draw_brightness()
                    self.ui_surface.fill((0, 0, 0, 0))

          def manage_events(self):
                    self.event_manager.update_window_events()
                    self.event_manager.update_size()
                    self.event_manager.update_fps_toggle()
                    self.event_manager.update_grab()
                    self.event_manager.update_changing_settings()

          def update_game_variables(self):
                    self.keys = pygame.key.get_pressed()
                    self.mouse_pos = pygame.mouse.get_pos()
                    self.correct_mouse_pos = (int(self.mouse_pos[0] * REN_RES[0] / self.display.width), int(self.mouse_pos[1] * REN_RES[1] / self.display.height))
                    self.mouse_state = pygame.mouse.get_pressed()
                    if not self.changing_settings: self.game_time += self.dt
                    if self.clock.get_fps() == 0: self.dt = 1 / 200
                    else: self.dt = 1 / self.clock.get_fps()

          def run_game(self):
                    if self.mainmenu.loop() is False: return None
                    while self.running:
                              self.clock.tick_busy_loop(self.fps)
                              self.update_game_variables()
                              self.manage_events()
                              self.update_groups()
                              self.draw_groups()
                              if self.immidiate_quit: return None
                              pygame.display.flip()
                    pygame.quit()
