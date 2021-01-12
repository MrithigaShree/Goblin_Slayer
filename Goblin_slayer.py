# initialize
import pygame

pygame.init()
screen_main = pygame.display.set_mode((800, 600))
# Title and icon
pygame.display.set_caption('Goblin Slayer')
icon_main = pygame.image.load('living-dead.png')
pygame.display.set_icon(icon_main)
font1 = pygame.font.Font('Comic Sans.ttf', 22)
font_big = pygame.font.Font('Comic Sans.ttf', 40)
pygame.display.init()
playerimg = pygame.image.load('player_pseudo.png')
Enemy_img = pygame.image.load('goblin.png')


def rules():
    header = font_big.render('GAME : GOBLIN SLAYER', 0, (50, 100, 245))
    rule = font1.render('RULES', 0, (255, 255, 255))    
    rule1 = font1.render('1.NO MORE THAN 15 MISSES', 0, (255, 255, 255))
    rule2 = font1.render('2.Don\'t let them get too close', 0, (255, 255, 255))
    rule3 = font1.render('3.Keys - ASD/ left , right and up', 0, (255, 255, 255))
    screen_main.blit(rule, (200, 200))
    screen_main.blit(rule1, (200, 250))
    screen_main.blit(rule2, (200, 300))
    screen_main.blit(rule3, (200, 350))
    screen_main.blit(header, (190, 25))
    screen_main.blit(playerimg, (100, 0))
    screen_main.blit(Enemy_img, (660, 0))


def button_start():
    # buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen_main, (0, 255, 0), (0, 550, 800, 50))
    button_text = font1.render('Slay \'em', True, (0, 0, 0))
    screen_main.blit(button_text, (360, 560))
    if 800 > mouse[0] and 550 + 50 > mouse[1] > 550:
        pygame.draw.rect(screen_main, (0, 150, 0), (0, 550, 800, 50))
        screen_main.blit(button_text, (360, 560))
        if click[0] == 1:
            return True


def button_replay():
    # buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen_main, (102, 15, 121), (0, 550, 800, 50))
    button_text = font1.render('Reslay', True, (0, 0, 0))
    screen_main.blit(button_text, (360, 560))
    if 800 > mouse[0] and 550 + 50 > mouse[1] > 550:
        pygame.draw.rect(screen_main, (118, 73, 128), (0, 550, 800, 50))
        screen_main.blit(button_text, (360, 560))
        if click[0] == 1:
            return True


def pause_button(miss_v, en_attack):
    if not (miss_v > 14 or en_attack == 1):
        text_play = font1.render('Click F10 to resume, esc to quit', True, (255, 255, 255))
        pygame.draw.rect(screen_main, (0, 0, 0), (763, 563, 40, 40))
        button = pygame.image.load('pause.png')
        screen_main.blit(button, (765, 565))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 763 + 40 > mouse[0] > 763 and 563 + 40 > mouse[1] > 563:
            pygame.draw.rect(screen_main, (48, 47, 46), (763, 563, 40, 40))
            screen_main.blit(button, (765, 565))
            if click[0] == 1:
                pause = True
                screen.blit(text_play, (250, 570))
                while pause:
                    for event_py in pygame.event.get():
                        if event_py.type == pygame.KEYDOWN:
                            if event_py.key == pygame.K_F10:
                                pause = False
                            if event_py.key == pygame.K_ESCAPE:
                                pygame.quit()
                    pygame.display.update()
                    if pause:
                        time.sleep(0)


def restart_play(miss_v, en_attack):
    if not (miss_v > 14 or en_attack == 1):
        pygame.draw.rect(screen_main, (0, 0, 0), (723, 563, 40, 40))
        button = pygame.image.load('replay.png')
        screen_main.blit(button, (725, 565))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 723 + 40 > mouse[0] > 723 and 563 + 40 > mouse[1] > 563:
            pygame.draw.rect(screen_main, (48, 47, 46), (723, 563, 40, 40))
            screen_main.blit(button, (725, 565))
            if click[0] == 1:
                return True


run = True
while run:
    screen_main.fill((0, 0, 0))
    rules()
    button_start()
    if button_start():
        import pygame
        import random
        import math
        import time

        # initialize
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        # background
        background = pygame.image.load('background.png')

        # Title and icon
        pygame.display.set_caption('Goblin Slayer')
        icon = pygame.image.load('living-dead.png')
        pygame.display.set_icon(icon)

        # player
        playerimg = pygame.image.load('player_pseudo.png')
        playerX = 370
        playerY = 480
        playerXdx = 0

        # score and misses
        score_value = 0
        miss_value = 0
        font = pygame.font.Font('Comic Sans.ttf', 22)
        textX = 10
        textY = 10
        over_font = pygame.font.Font('Comic Sans.ttf', 50)
        invfont = pygame.font.Font('Comic Sans.ttf', 30)

        enemy_attack = 0  # mainly for not having play button over replay button


        def invaded():
            invade = invfont.render('gotcha - goblins rule', True, (255, 0, 0))
            screen.blit(invade, (200, 200))


        def show_score(x_pos, y_pos):
            diamondimg = pygame.image.load('diamond_blue.png')
            screen.blit(diamondimg,(x_pos,y_pos))
            score_seen = font.render('      :' + str(score_value), True, (9, 224, 249))
            screen.blit(score_seen, (x_pos, y_pos))


        def show_miss():  # misses
            heartimg = pygame.image.load('heart.png')
            broken_heart=pygame.image.load('broken-heart.png')
            value=790 # for blitting purposes
            for i in range(0,5-miss_value):
                value -= 27
                screen.blit(heartimg,(value,10))
            value_broken_heart = 627
            if miss_value >0:
                for i in range(0,miss_value):
                    value_broken_heart+=27
                    screen.blit(broken_heart,(value_broken_heart,10))                  
                              


        def game_over_text():
            global run
            over_text = over_font.render('GAME OVER', True, (255, 255, 255))
            screen.blit(over_text, (200, 250))


        def miss_text():
            text = font.render('slay again man', True, (255, 0, 0))
            screen.blit(text, (200, 200))


        # enemy
        enemyImg = []
        enemyX = []
        enemyY = []
        enemyXdx = []
        enemyYdx = []
        num_of_enemies = 6
        for i in range(num_of_enemies):
            enemyImg.append(pygame.image.load('goblin.png'))
            enemyX.append(random.randint(5, 730))
            enemyY.append(random.randint(50, 150))
            enemyXdx.append(1.5)
            enemyYdx.append(30)

        # bullet
        bulletImg = pygame.image.load('dagger.png')
        bulletX = 0
        bulletY = 480
        bulletYdx = 10
        bullet_state = 'ready'  # not seen


        def player(playerx, playery):
            screen.blit(playerimg, (playerx, playery))


        def enemy(a, b, c):
            screen.blit(enemyImg[c], (a, b))


        def fire_bullet(x_cor, y_cor):
            global bullet_state
            bullet_state = 'fire'
            screen.blit(bulletImg, (x_cor, y_cor))


        def collided(enemyx, enemyy, bulletx, bullety):
            distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
            if distance < 35:
                return True


        # main loop
        running = True
        while running:
            # screen.fill((0, 0, 0))

            # background
            screen.blit(background, (-0, -0))
            playerX += playerXdx
            for event_main in pygame.event.get():
                if event_main.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event_main.type == pygame.KEYDOWN:
                    if event_main.key == pygame.K_RIGHT or event_main.key == pygame.K_d:
                        playerXdx = 1.9
                    elif event_main.key == pygame.K_LEFT or event_main.key == pygame.K_a:
                        playerXdx = -1.9
                    elif event_main.key == pygame.K_UP or event_main.key == pygame.K_s:
                        if bullet_state == 'ready':
                            bulletX = playerX
                            fire_bullet(bulletX, playerY)
                    elif event_main.key == pygame.K_ESCAPE:
                        pygame.quit()
                        running = False
                else:
                    playerXdx = 0

            # player boundary
            if playerX <= 0:
                playerX = 0
            elif playerX >= 730:
                playerX = 730
            for i in range(num_of_enemies):
                # Game over
                if enemyY[i] > 400:
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    playerY = 2000
                    bullet_state = 'ready'
                    # misses(
                    enemy_attack = 1  # for not having play button on replay button
                    if miss_value < 5:
                        invaded()
                    game_over_text()
                    button_replay()
                    if button_replay():
                        running = False
                        break
                    break
                enemyX[i] += enemyXdx[i]
                # border checks for enemies
                if enemyX[i] <= 0:
                    enemyY[i] += enemyYdx[i]
                    enemyXdx[i] = 1.8
                elif enemyX[i] >= 730:
                    enemyY[i] += enemyYdx[i]
                    enemyXdx[i] = -1.8

                # collision
                collision = collided(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    bulletY = 480
                    bullet_state = 'ready'
                    score_value += 1
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = random.randint(50, 150)
                enemy(enemyX[i], enemyY[i], i)
            # misses
            if bulletY <= 0:
                bulletY = 480
                bullet_state = 'ready'
                miss_value += 1
            # when bullet is fired
            if bullet_state == 'fire':
                bulletY -= bulletYdx
                fire_bullet(bulletX, bulletY)
            # end of game due to too many misses
            if miss_value > 4:
                miss_text()
                game_over_text()
                button_replay()
                if button_replay():
                    running = False
                    break
                for i in range(num_of_enemies):
                    enemyY[i] = 2000
            # all the fn calls
            player(playerX, playerY)
            show_score(textX, textY)
            show_miss()
            if pause_button(miss_value, enemy_attack):
                pass
            if restart_play(miss_value, enemy_attack):
                running = False
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            rules()

            break
    pygame.display.update()
