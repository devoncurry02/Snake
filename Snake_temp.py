import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
run = True
dt = 0

position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", position, 20, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        position.y -= 300 * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        position.y += 300 * dt
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        position.x -= 300 * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        position.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()