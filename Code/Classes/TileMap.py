from pygame import Vector2

from Code.Utilities.Grid import *


class Tile:
          def __init__(self, tile_type, position):
                    self.tile_type = tile_type
                    self.position = Vector2(position)
                    self.size = General_Settings['tilemap_size']
                    self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
                    self.images = Tile_Images[tile_type]

          def draw(self, surface, offset, frame):
                    draw_position = self.position - offset
                    surface.blit(self.images[int(frame % len(self.images))], draw_position)


class TileMap:
          def __init__(self, game):
                    self.game = game
                    self.grid = SpatialHash(game)

                    self.tile_size = General_Settings['tilemap_size']
                    self.width = GAME_SIZE[0] // self.tile_size
                    self.height = GAME_SIZE[1] // self.tile_size

                    self.animation_speed = General_Settings["animation_speed"]
                    self.frames = {tile_type: 0 for tile_type in Tile_Images.keys()}

                    self.terrain_generator()

                    self.grid.rebuild()

          def add_tile(self, tile_type, position):
                    tile = Tile(tile_type, (position[0] * self.tile_size, position[1] * self.tile_size))
                    self.grid.insert(tile)

          def draw(self):
                    for tile_type in self.frames:
                              self.frames[tile_type] += self.game.dt * self.animation_speed
                    for tile in self.grid.window_query():
                              tile.draw(self.game.display_screen, self.game.window.offset_rect.topleft, self.frames[tile.tile_type])

          @staticmethod
          def get_tile_type(x, y):
                    noise_value = Perlin_Noise["terrain_generation"]([x * 0.05, y * 0.05])
                    if noise_value < -0.2:
                              return "Water_Tile"
                    elif noise_value < 0:
                              return "Sand_Tile"
                    elif noise_value < 0.3:
                              return "Grass_Tile"
                    else:
                              return "Mountain_Tile"

          def get_tile_at(self, world_position):
                    grid_x = int(world_position[0] // self.tile_size)
                    grid_y = int(world_position[1] // self.tile_size)
                    rect = pygame.Rect(world_position[0] , world_position[1], self.tile_size, self.tile_size)
                    for tile in self.grid.query(rect):
                              if tile.position.x == grid_x * self.tile_size and tile.position.y == grid_y * self.tile_size:
                                        return tile
                    return None

          def update_tile(self, world_position, new_tile_type):
                    tile = self.get_tile_at(world_position)
                    if tile:
                              self.grid.remove(tile)
                              self.add_tile(new_tile_type,
                                            (tile.position.x // self.tile_size, tile.position.y // self.tile_size))

          def terrain_generator(self):
                    for x in range(self.width):
                              for y in range(self.height):
                                        tile_type = self.get_tile_type(x, y)
                                        self.add_tile(tile_type, (x, y))
