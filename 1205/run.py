# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()

# 畫布大小
screen = pygame.display.set_mode((1280, 400))

BLACK = (0,0,0)

# 載入圖片
img_aa = pygame.image.load("haa.png")

img_aa=pygame.transform.scale(pygame.image.load("haa.png"),(100,200))
img_bb=pygame.transform.scale(pygame.image.load("dinorun.png"),(100,200))
img_dinorun = [img_aa,img_bb]

img_dinoduck1=pygame.transform.scale(pygame.image.load("dinoduck.png"),(100,200))
img_dinoduck2=pygame.transform.scale(pygame.image.load("dinoduck 1.png"),(100,200))
img_dinoduck =  [img_dinoduck1,img_dinoduck2]

img_bird=pygame.transform.scale(pygame.image.load("Bird1.png"),(40,40))
img_bird2=pygame.transform.scale(pygame.image.load("Bird2.png"),(40,40))
img_birdrun = [img_bird,img_bird2]


img_cactus = pygame.image.load("cc.jpeg")
img_cactus=pygame.transform.scale(img_cactus,(50,50))

img_track = pygame.image.load("track.png")
screen.fill((255,255,255))
screen.blit(img_track,(0,370))

# 設定角色
dino_rect = img_aa.get_rect()
dino_rect.x = 50
dino_rect.y = 200
is_jumping =False
is_ducking=False
jump = 25
nowjump =jump
g = 1

cactus_rect = img_cactus.get_rect()
cactus_rect.x = 1500
cactus_rect.y = 330
speed = 5

bird_rect=img_bird.get_rect()
bird_rect.x = 1000
bird_rect.y = 200
initspeed = 5
speed=initspeed

# 設定分數
score = 0
highscore =0 # 最高紀錄
font = pygame.font.Font(None,36)

level=0
speedlist=[5,6,7,8]

clock = pygame.time.Clock()
running = True
gameover = False

frame=0
lastime=0




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score += 1
    if score>2000:
        speed+=1 

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jumping = True
                if event.key == pygame.K_r:
                    score = 0
                    bird_rect.x=2000
                    cactus_rect.x = 2000
                    gameover = False
                if event.key==pygame.K_DOWN:
                    dino_rect.y=290
                    is_ducking=True
            if event.type==pygame.KEYUP:
                dino_rect.y=200
                if is_ducking:
                    is_ducking=False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping = True
                if gameover:
                    score = 0
                    cactus_rect.x = 2000
                    gameover = False


                    

    if not gameover:

        if score%400==0:
            speed+=1
        
        if is_jumping:
            dino_rect.y -= nowjump
            nowjump -= g
            if dino_rect.y>200:
                dino_rect.y=200
                nowjump = jump
                is_jumping = False

        cactus_rect.x -= speed
        bird_rect.x-=speed
        if cactus_rect.x < 0:
            cactus_rect.x=random.randrange(1280, 3000)
            
        if bird_rect.x < 0:
            bird_rect.x=random.randrange(1280, 3000)
            

        if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):
            if score > highscore:
                highscore = score
            gameover = True
            speed=initspeed
        if score>1000:
            speed = speedlist[1]
            level = 1
        elif score >2000:
            speed = speedlist[2]
            level =2
        elif score >3000:
            speed = speedlist[3]
            level = 3

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))


        score_show = font.render(f"Score: {score}",True, BLACK)
        screen.blit(score_show,(10,10))

        level_show = font.render(f"Level: {level}",True, BLACK)
        highscore_show = font.render(f"Hi Score: {highscore}",True, BLACK)
        screen.blit(highscore_show,(10,30))
        
        if gameover:
            gameover_show = font.render(f"Game Over",True, BLACK)
            screen.blit(gameover_show,(550,150))
        
        nowtime=pygame.time.get_ticks()
        if nowtime-lastime>300:
            frame=(frame+1)%2
            lastime=nowtime
        if is_ducking:
            screen.blit(img_dinoduck[frame],dino_rect)
        else:
            screen.blit(img_dinorun[frame],dino_rect)

        
        # RENDER YOUR GAME HERE
        # screen.blit(img_dino,dino_rect)
        # screen.blit(img_dinorun[frame],dino_rect)
        screen.blit(img_cactus,cactus_rect)
        screen.blit(img_birdrun[frame],bird_rect)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()