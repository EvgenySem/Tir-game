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
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, WIDTH - target_width)
                target_y = random.randint(0, HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()