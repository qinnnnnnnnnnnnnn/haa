import pygame

# pygame setup
pygame.init()
#畫布大小
screen = pygame.display.set_mode((1280, 400))

#載入圖片
img_aa=pygame.image.load("haa.png")
img_bb=pygame.image.load("cc.jpeg")
img_aa=pygame.transform.scale(img_aa,(100,200))
img_bb=pygame.transform.scale(img_bb,(40,40))
#設定角色
aa_rect=img_aa.get_rect()
aa_rect.x=50
aa_rect.y=200
is_jumping=False
jump=12
nowjump=jump
g=1

bb_rect=img_bb.get_rect()
bb_rect.x=1200
bb_rect.y=360
speed=5

score=0
font=pygame.font.Font(None,36)

clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    is_jumping=True
    if is_jumping:
        aa_rect.y-=nowjump
        nowjump-=g
        if aa_rect.y>200:
            aa_rect.y=200
            nowjump=jump
            is_jumping=False

    bb_rect.x-=speed
    if bb_rect.x<0:
        bb_rect.x=1200

            
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,255,255))


    score_show=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_show,(10,10))
    # RENDER YOUR GAME HERE

    screen.blit(img_aa,aa_rect)
    screen.blit(img_bb,bb_rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()