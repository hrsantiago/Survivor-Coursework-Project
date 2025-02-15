from Code.Variables.Variables import *

class main_camera:
          def set_attributes(self, attributes):
                    for key, value in attributes.items():
                              setattr(self, key, value)


class CameraManager(main_camera):
          def __init__(self, game):
                    self.game = game
                    self.res = REN_RES

                    self.set_attributes(Window_Attributes)

                    self.target_offset = v2(0, 0)
                    self.current_offset = v2(0, 0)

                    self.pos = v2(self.game.player.pos.x - self.res[0] / 2, self.game.player.pos.y - self.res[1] / 2)
                    self.rect = pygame.Rect(self.pos.x, self.pos.y, self.res[0], self.res[1])
                    self.offset_rect = self.rect.copy()

                    self.shake_start_time = 0
                    self.shake_magnitude = 0
                    self.shake_duration = 0
                    self.shake_seed = random.random() * 1000
                    self.shake_direction = v2(1, 1)

                    self.noise_map = PerlinNoise(Map_Config["camera_shake_map"][0], random.randint(0, 100000))

          def move(self, dx, dy, move_horizontally, move_vertically):
                    if move_horizontally:
                              self.pos.x += dx * self.game.player.current_vel * self.game.dt
                    if move_vertically:
                              self.pos.y += dy * self.game.player.current_vel * self.game.dt

                    self.update_mouse_smoothing()
                    rounded_offset = self.calculate_offset()
                    shake_offset = self.calculate_shake()
                    self.update_offset_rect(rounded_offset, shake_offset)
                    self.ensure_player_in_bounds()

          def update_mouse_smoothing(self):
                    mouse_target = v2(self.game.correct_mouse_pos[0] - 0.5 * REN_RES[0],
                                      self.game.correct_mouse_pos[1] - 0.5 * REN_RES[1])

                    dt = min(self.game.dt, 1 / 20)
                    self.mouse_smoothing = v2(
                              self.lerp(self.mouse_smoothing.x, mouse_target.x,
                                        self.window_mouse_smoothing_amount * dt),
                              self.lerp(self.mouse_smoothing.y, mouse_target.y,
                                        self.window_mouse_smoothing_amount * dt)
                    )

                    self.mouse_smoothing.x = 0 if abs(
                              self.mouse_smoothing.x) < self.deadzone else self.mouse_smoothing.x
                    self.mouse_smoothing.y = 0 if abs(
                              self.mouse_smoothing.y) < self.deadzone else self.mouse_smoothing.y

          def calculate_offset(self):
                    self.target_offset = v2(
                              self.window_max_offset * int(self.mouse_smoothing.x),
                              self.window_max_offset * int(self.mouse_smoothing.y)
                    )

                    self.current_offset = v2(
                              self.lerp(self.current_offset.x, self.target_offset.x, self.lerp_speed * self.game.dt),
                              self.lerp(self.current_offset.y, self.target_offset.y, self.lerp_speed * self.game.dt)
                    )

                    return v2(round(self.current_offset.x), round(self.current_offset.y))

          def update_offset_rect(self, rounded_offset, shake_offset):
                    self.offset_rect.x = max(0, min(self.pos.x + rounded_offset.x + shake_offset.x,
                                                    GAME_SIZE[0] - self.res[0]))
                    self.offset_rect.y = max(0, min(self.pos.y + rounded_offset.y + shake_offset.y,
                                                    GAME_SIZE[1] - self.res[1]))

          def ensure_player_in_bounds(self):
                    player = self.game.player
                    player_left = player.pos.x - self.offset_rect.x - player.res[0] / 2
                    player_right = player_left + player.res[0]
                    player_top = player.pos.y - self.offset_rect.y - player.res[1] / 2
                    player_bottom = player_top + player.res[1]

                    if player_left < player.offset[0]:
                              self.offset_rect.x += player_left - player.offset[0]
                    elif player_right > self.res[0] - player.offset[2]:
                              self.offset_rect.x += player_right - (self.res[0] - player.offset[2])

                    if player_top < player.offset[1]:
                              self.offset_rect.y += player_top - player.offset[1]
                    elif player_bottom > self.res[1] - player.offset[3]:
                              self.offset_rect.y += player_bottom - (self.res[1] - player.offset[3])

                    self.offset_rect.x = max(0, min(self.offset_rect.x, GAME_SIZE[0] - self.res[0]))
                    self.offset_rect.y = max(0, min(self.offset_rect.y, GAME_SIZE[1] - self.res[1]))

          def calculate_shake(self):
                    current_time = self.game.game_time
                    elapsed_time = current_time - self.shake_start_time

                    if elapsed_time > self.shake_duration:
                              self.shake_duration = 0
                              return v2(0, 0)

                    fade_out = 1 - (elapsed_time / self.shake_duration)
                    sin_value = math.sin(self.shake_speed * (self.shake_seed + elapsed_time))

                    noise_x = self.get_2d_noise(self.shake_seed + elapsed_time, 0)
                    noise_y = self.get_2d_noise(0, self.shake_seed + elapsed_time)
                    noise_offset = v2(noise_x, noise_y)

                    direction = (
                            self.shake_direction + noise_offset * self.reduced_screen_shake).normalize()

                    shake_offset = direction * sin_value * self.shake_magnitude * fade_out
                    return v2(int(shake_offset.x), int(shake_offset.y))

          def get_2d_noise(self, x, y):
                    scaled_x, scaled_y = x * Map_Config["camera_shake_map"][1], y * Map_Config["camera_shake_map"][1]
                    return self.noise_map([scaled_x, scaled_y])

          def add_screen_shake(self, duration, magnitude):
                    if self.shake_duration + self.shake_start_time < self.game.game_time:
                              self.shake_magnitude = 0
                    if magnitude > self.shake_magnitude:
                              self.shake_duration = duration
                              self.shake_magnitude = magnitude
                              self.shake_start_time = self.game.game_time
                              self.shake_seed = self.game.game_time
                              self.shake_direction = v2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

          @staticmethod
          def lerp(start, end, amount):
                    return start + (end - start) * amount
