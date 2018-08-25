import pygame
from random import shuffle

pygame.init()
disp_width = 1200
disp_height = 600
win = pygame.display.set_mode((disp_width, disp_height))

pygame.display.set_caption('Goalkeeper Game')

bg = pygame.image.load('bg.png')
keep_positions = [(pygame.image.load('keep_1.png'), 20, 0),
                (pygame.image.load('keep_2.png'), 378, 0),
                (pygame.image.load('keep_3.png'), 1155, 590),
                (pygame.image.load('keep_4.png'), 230, 345),
                (pygame.image.load('keep_5.png'), 565, 294),
                (pygame.image.load('keep_6.png'), 1155, 590)]
ball = pygame.image.load('ball.png')

width_keep = 70
height_keep = 126
width_goal = 800
height_goal = 240
x_pos_keep = (disp_width - width_keep) // 2
y_pos_keep = (disp_height - height_goal) // 2 + height_goal - height_keep
x_pos_goal = (disp_width - width_goal) // 2
y_pos_goal = (disp_height - height_goal) // 2
speed_keep_width = (width_goal - width_keep) // 2
speed_keep_height = height_goal - height_keep

left = False
right = False
up = False
down = False

cycle_time = 1000
shots = [(20, 0, 1, 1), (378, 0, 1, 1), (1155, 0, -1, 1), (20, 590, 1, -1), (378, 560, 1, -1), (1155, 590, -1, -1)]
keep_position = 4

run = True
while run:
    pygame.time.delay(cycle_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    run_ball = True
    i = 0
    shuffle(shots)
    while run_ball:
        pygame.time.delay(cycle_time // 20)
        win.blit(bg, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keep_position > 2:
                keep_position = max(3, keep_position - 1)
            else:
                keep_position = max(0, keep_position - 1)
        if keys[pygame.K_RIGHT]:
            if keep_position < 3:
                keep_position = min(2, keep_position + 1)
            else:
                keep_position = min(5, keep_position + 1)
        if keys[pygame.K_UP]:
            if keep_position > 2:
                keep_position -= 3
        if keys[pygame.K_DOWN]:
            if keep_position < 3:
                keep_position += 3

        win.blit(keep_positions[keep_position][0], (keep_positions[keep_position][1], keep_positions[keep_position][2]))
        win.blit(ball, (shots[0][0] + 10.5 * i * shots[0][2], shots[0][1] + 10.5 * i * shots[0][3]))
        pygame.display.update()
        i += 1
        if i > 20:
            run_ball = False

pygame.quit()
