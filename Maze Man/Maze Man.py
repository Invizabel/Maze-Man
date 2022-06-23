from pygame import *

import math
import numpy as np
import pygame
import random

maze = np.array([])

size = 1000

for i in range(0, size * size):
    rand = random.randint(0,1)
    maze = np.append(maze, [rand])
    
maze = maze.reshape(size, size)

#draw screen
pygame.init()
screen_size = pygame.display.Info()
my_screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
my_screen.fill("cyan")

def game():
    maze_man = pygame.image.load("Maze Man.png")
    maze_man = pygame.transform.scale(maze_man,(50, 50))

    player_health = 3
    player_x = screen_size.current_w / 2
    player_y = screen_size.current_h / 2
    
    running = True

    maze_count_x = 0
    maze_count_y = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        my_screen.fill("cyan")

        for i in range(0, size):
            for ii in range(0, size):
                maze_count_x += 1

                if maze_count_x == size:
                    maze_count_x = 0
                    maze_count_y += 1

                if maze_count_y == size:
                    maze_count_x = 0
                    maze_count_y = 0
                    
                if math.ceil(maze[i, ii]) == 1:
                    pygame.draw.rect(my_screen, "red", pygame.Rect(maze_count_x * 100, maze_count_y * 100, 50, 50))

        #keyboard input
        keyboard = pygame.key.get_pressed()

        left_mouse = pygame.mouse.get_pressed()[0]
        right_mouse = pygame.mouse.get_pressed()[2]

        if keyboard[pygame.K_LEFT]:
            player_x -= screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_a]:
            player_x -= screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_RIGHT]:
            player_x += screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_d]:
            player_x += screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_UP]:
            player_y -= screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_w]:
            player_y -= screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_DOWN]:
            player_y += screen_size.current_w / 1000
            #my_screen.fill("cyan")

        if keyboard[pygame.K_s]:
            player_y += screen_size.current_w / 1000
            #my_screen.fill("cyan")

        #quit game
        if keyboard[pygame.K_ESCAPE]:
            running = False

        #render player
        if player_health > 0:
            my_screen.blit(maze_man, (player_x, player_y))
            
        pygame.display.flip()

    pygame.quit()

game()
