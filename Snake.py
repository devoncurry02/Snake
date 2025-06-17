import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 800))
run = True
clock = pygame.time.Clock()
time = 1
direction = "right"
x = screen.get_width() // 2 - 5
y = screen.get_height() // 2 - 5
class Apple:
    def __init__(self):
        self.pygame.draw.rect(screen, "red", pygame.Rect(x, y, 20, 20))
        self.relocate()
    def relocate(self):
        self.apple_pos = pygame.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("black")
    
    Apple().__init__()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 300 * time
        direction = "up"
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 300 * time
        direction = "down"
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 300 * time
        direction = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 300 * time
        direction = "right"
    else: 
        if direction == "up":
            y -= 300 * time
        elif direction == "down":
            y += 300 * time
        elif direction == "left":
            x -= 300 * time
        elif direction == "right":
            x += 300 * time

    pygame.draw.rect(screen, "green", pygame.Rect(x, y, 20, 20))

    pygame.display.flip()

    time = clock.tick(10) / 1000