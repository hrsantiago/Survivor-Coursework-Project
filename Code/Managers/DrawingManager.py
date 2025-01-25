import pygame
from pygame import Surface
from typing import List, Tuple


class DrawingManager:
          def __init__(self, game):
                    self.game = game
                    self.drawables = []
                    self.batch_surface = pygame.Surface(self.game.display_surface.get_size(), pygame.SRCALPHA)

          def transparent_objects(self):
                    player_rect = self.game.player.rect
                    player_bottom = player_rect.bottom

                    for thing in self.game.object_manager.grid.query(player_rect):
                              if thing.rect.colliderect(player_rect):
                                        dy = thing.rect.bottom - player_bottom
                                        squared_distance = dy * dy
                                        greatest_side = thing.image.get_height()
                                        alpha = max(100, min(int(squared_distance / (greatest_side * greatest_side) * 255), 255))

                                        if player_bottom > thing.rect.bottom:
                                                  alpha = 255

                                        thing.image = self.game.methods.get_transparent_image(thing.original_image, alpha)
                              else:
                                        thing.image = thing.original_image

          def draw(self):
                    self.transparent_objects()

                    self.drawables.extend(self.game.object_manager.grid.window_query())
                    self.drawables.extend(self.game.enemy_manager.grid.window_query())
                    self.drawables.extend([rain_droplet for rain_droplet in self.game.rain_manager.grid.window_query() if rain_droplet.hit_ground])
                    self.drawables.append(self.game.player)

                    self.drawables.sort(key=lambda obj: obj.rect.bottom)

                    for drawable in self.drawables:
                              drawable.draw()

                    self.drawables.clear()

          def batch_draw(self, surface: Surface):
                    drawables_data: List[Tuple[Surface, Tuple[int, int]]] = [
                              (drawable.image, (drawable.rect.x - self.game.camera.offset_rect.x,
                                                drawable.rect.y - self.game.camera.offset_rect.y))
                              for drawable in self.drawables
                    ]
                    surface.blits(drawables_data)