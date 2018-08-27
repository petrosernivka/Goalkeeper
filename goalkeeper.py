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

shots = [(20, 0, 1, 1, 0), (378, 0, 1, 1, 1), (1155, 0, -1, 1, 2),
        (20, 590, 1, -1, 3), (378, 560, 1, -1, 4), (1155, 590, -1, -1, 5)]
keep_position = 4
ball_run_index = 0
scores = 0

myfont = pygame.font.SysFont('Comic Sans MS', 60)

win.blit(bg, (0, 0))
scores_text = myfont.render('To start the game, press any key', False, (255, 255, 255))
win.blit(scores_text, (140,40))
pygame.display.update()

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run = False

run = True
while run:
    cycle_time = 150 - min(3, scores // 10) * 20

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

    if ball_run_index > 210:
        pygame.time.delay(700)
        ball_run_index = 0
        shuffle(shots)

    win.blit(bg, (0, 0))
    win.blit(keep_positions[keep_position][0], (keep_positions[keep_position][1], keep_positions[keep_position][2]))

    if ball_run_index >= 210:
        if shots[0][4] == keep_position:
            win.blit(star_green, (shots[0][0] + 210 * shots[0][2] - 5, shots[0][1] + 210 * shots[0][3] - 5))
            scores += 1
        else:
            win.blit(star_red, (shots[0][0] + 210 * shots[0][2] - 5, shots[0][1] + 210 * shots[0][3] - 5))
            win.blit(ball, (shots[0][0] + min(210, ball_run_index) * shots[0][2], shots[0][1] + min(210, ball_run_index) * shots[0][3]))
            run = False

    win.blit(ball, (shots[0][0] + min(210, ball_run_index) * shots[0][2], shots[0][1] + min(210, ball_run_index) * shots[0][3]))

    scores_text = myfont.render('Scores: ' + str(scores), False, (0, 30, 0))
    win.blit(scores_text, (450,500))

    pygame.display.update()
    ball_run_index += 21

pygame.time.delay(3000)
pygame.quit()
