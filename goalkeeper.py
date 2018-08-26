import pygame
from random import shuffle

pygame.init()
disp_width = 1200
disp_height = 600
win = pygame.display.set_mode((disp_width, disp_height))

pygame.display.set_caption('Goalkeeper Game')

bg = pygame.image.load('bg.png')
ball = pygame.image.load('ball.png')
star_green = pygame.image.load('star_green.png')
star_red = pygame.image.load('star_red.png')
keep_positions = [(pygame.image.load('keep_1.png'), 223, 202),
                (pygame.image.load('keep_2.png'), 563, 210),
                (pygame.image.load('keep_3.png'), 815, 202),
                (pygame.image.load('keep_4.png'), 230, 345),
                (pygame.image.load('keep_5.png'), 565, 294),
                (pygame.image.load('keep_6.png'), 802, 343)]

cycle_time = 150
shots = [(20, 0, 1, 1), (378, 0, 1, 1), (1155, 0, -1, 1), (20, 590, 1, -1), (378, 560, 1, -1), (1155, 590, -1, -1)]
keep_position = 4
ball_run_index = 0

run = True
while run:
    pygame.time.delay(cycle_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

    if ball_run_index > 273:
        ball_run_index = 0
        shuffle(shots)

    win.blit(bg, (0, 0))
    win.blit(keep_positions[keep_position][0], (keep_positions[keep_position][1], keep_positions[keep_position][2]))

    # if ball_run_index > 210: #and keeper is in same position as ball_run_index
    #     win.blit(ball, (shots[0][0] + min(210, ball_run_index) * shots[0][2], shots[0][1] + min(210, ball_run_index) * shots[0][3]))

    win.blit(ball, (shots[0][0] + min(210, ball_run_index) * shots[0][2], shots[0][1] + min(210, ball_run_index) * shots[0][3]))
    pygame.display.update()
    ball_run_index += 21

pygame.quit()
