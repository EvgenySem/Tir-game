import pygame, random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

target_img = pygame.image.load('img/apple.png')
target_width = 80
target_height = 80
target_x = random.randint(0, WIDTH - target_width)
target_y = random.randint(0, HEIGHT - target_height)

bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

run = True
while run:
    pass


pygame.quit()