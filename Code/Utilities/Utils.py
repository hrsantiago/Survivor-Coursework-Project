import functools
import math
import os
import random
import numpy as np
import pygame


def random_xy(rect1, rect2, sprite_width, sprite_height):
          while True:
                    x = random.randint(rect1.left, rect1.right - sprite_width)
                    y = random.randint(rect1.top, rect1.bottom - sprite_height)
                    if not rect2.collidepoint(x, y): return x, y


def change_by_diff(number, diff):
          diff = random.random() * diff
          if random.randint(0, 1) == 0:
                    return number - diff
          else:
                    return number + diff


def change_by_random(number, amount):
          if random.random() < 0.5:
                    return number - random.randint(0, amount)
          else:
                    return number + random.randint(0, amount)


def perfect_outline(img, outline_color=(255, 255, 255)):
          mask = pygame.mask.from_surface(img)
          mask_outline = mask.outline()
          mask_surf = pygame.Surface(img.get_size(), pygame.SRCALPHA)

          for x, y in mask_outline:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                              mask_surf.set_at((x + dx, y + dy), outline_color)

          outlined_img = img.copy()
          outlined_img.blit(mask_surf, (0, 0))
          outlined_img.blit(img)
          return outlined_img


def lookup_colour(colour):
          color_list = [(c, v) for c, v in pygame.color.THECOLORS.items() if colour in c]
          for colour in color_list: print(colour)


def get_unique_filename(path):
          root, ext = os.path.splitext(path)
          counter = 1
          while os.path.exists(path):
                    path = f"{root}_{counter}{ext}"
                    counter += 1
          return path


def rename_files_recursive(directory):
          for root, dirs, files in os.walk(directory):
                    for filename in files:
                              if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                                        new_filename = filename.lower().replace(' ', '_')
                                        if filename != new_filename:
                                                  old_path = os.path.join(root, filename)
                                                  new_path = os.path.join(root, new_filename)
                                                  if os.path.exists(new_path):
                                                            new_path = get_unique_filename(new_path)
                                                  os.rename(old_path, new_path)
                                                  print(f"Renamed: {old_path} -> {new_path}")

def create_weapon_settings(vel, spread, reload_time, fire_rate, clip_size, lifetime, lifetime_randomness,
                           damage, distance, friction, animation_speed, spread_time,
                           pierce, shots, name):
          return {
                    "vel": vel,
                    "spread": spread,
                    "reload_time": reload_time,
                    "fire_rate": fire_rate,
                    "clip_size": clip_size,
                    "lifetime": lifetime,
                    "lifetime_randomness": lifetime_randomness,
                    "damage": damage,
                    "distance": distance,
                    "friction": friction,
                    "animation_speed": animation_speed,
                    "spread_time": spread_time,
                    "pierce": pierce,
                    "shots": shots,
                    "name": name
          }


def create_button(text_input, pos, image, res=(46, 15), axis="y", axisl="max", text_pos="center", speed=900,
                  base_colour=(255, 255, 255),
                  hovering_colour=(255, 0, 0), hover_slide=True, hover_offset=10, hover_speed=20,
                  current_hover_offset=0, active=False, on=False):
          return {
                    "text_input": text_input,
                    "pos": pos,
                    "res": res,
                    "axis": axis,
                    "axisl": axisl,
                    "text_pos": text_pos,
                    "image": image,
                    "speed": speed,
                    "base_colour": base_colour,
                    "hovering_colour": hovering_colour,
                    "hover_slide": hover_slide,
                    "hover_offset": hover_offset,
                    "hover_speed": hover_speed,
                    "current_hover_offset": current_hover_offset,
                    "active": active,
                    "on": on
          }


def create_slider(pos, image, text_input, min_value, max_value, initial_value, axis="y", axisl="max", text_pos="right",
                  circle_base_colour=(255, 255, 255), circle_hovering_color=(255, 0, 0), speed=900,
                  hover_slide=False, hover_offset=10, hover_speed=20, current_hover_offset=0, active=False,
                  res=(46, 15), base_colour=(255, 255, 255),
                  is_dragging=False, line_colour=(120, 120, 120), line_thickness=2):
          return {
                    "text_input": text_input,
                    "pos": pos,
                    "image": image,
                    "min_value": min_value,
                    "max_value": max_value,
                    "value": initial_value,
                    "axis": axis,
                    "axisl": axisl,
                    "text_pos": text_pos,
                    "circle_base_colour": circle_base_colour,
                    "circle_hovering_colour": circle_hovering_color,
                    "speed": speed,
                    "hover_slide": hover_slide,
                    "hover_offset": hover_offset,
                    "hover_speed": hover_speed,
                    "current_hover_offset": current_hover_offset,
                    "active": active,
                    "res": res,
                    "base_colour": base_colour,
                    "is_dragging": is_dragging,
                    "line_colour": line_colour,
                    "line_thickness": line_thickness
          }


def create_spark_settings(spread, scale, colour, amount, min_vel, max_vel):
          return {
                    "spread": spread,
                    "scale": scale,
                    "colour": colour,
                    "amount": amount,
                    "min_vel": min_vel,
                    "max_vel": max_vel,
          }


def create_enemy_settings(name, health, vel, damage, stopping_distance,
                          steering_strength, friction, animation_speed, hit_cooldown, separation_radius, separation_strength):
          return {
                    'name': name,
                    'health': health,
                    'vel': vel,
                    'damage': damage,
                    'stopping_distance': stopping_distance,
                    'steering_strength': steering_strength,
                    'friction': friction,
                    'animation_speed': animation_speed,
                    "hit_cooldown": hit_cooldown,
                    "separation_radius": separation_radius,
                    "separation_strength": separation_strength,
          }
