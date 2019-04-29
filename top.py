from main import run_game
import pygame

win_file = "/Users/Ian/Desktop/won.png"

levels = ["/Users/Ian/Desktop/map1.png", "/Users/Ian/Desktop/map2.png",
          "/Users/Ian/Desktop/map3.png", "/Users/Ian/Desktop/map4.png"]
enemy_xs = [600, 30, 1170, 259]
enemy_ys = [100, 260, 690, 604]
cat_spd = [0, 0, 0, 0]
bullet_spd = [1.5, 1.5, 1.5, 1.5]
cat_x =[590, 53, 600, 1150]
cat_y = [883, 850, 860, 870]


for y in range(0, len(levels)):
   run_game(levels[y], enemy_xs[y], enemy_ys[y], bullet_spd[y], cat_spd[y], cat_x[y], cat_y[y])

#When you win the game
run_game(win_file)
