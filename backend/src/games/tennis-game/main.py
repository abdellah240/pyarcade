import pygame,asyncio,sys
from player import Player
from ball import Ball

pygame.init()

#Constants
SCREEN_SIZE = [700,700]
NET_SIZE= [5,SCREEN_SIZE[1]]
PADDING = 15

screen = pygame.display.set_mode((700,700))

#INITIALIZE OBJECTS
p1=Player(SCREEN_SIZE[0]/4-Player.SIZE[0],SCREEN_SIZE[1]/2-Player.SIZE[1],'./media/images/PLAYER1.png')
p1.draw()
p2=Player(3*SCREEN_SIZE[0]/4+Player.SIZE[0], SCREEN_SIZE[1]/2-Player.SIZE[1], './media/images/PLAYER2.png')
p2.draw()
ball= Ball(p1.rect.right+PADDING, p1.rect.centery,'./media/images/BALL.png')
ball.draw()
net = pygame.Rect(SCREEN_SIZE[0]/2, 0, *NET_SIZE)

clock = pygame.time.Clock()


async def main():
#GAME LOOP
    while True:
        screen.fill(color=(86, 125, 70))

        #Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #INPUT
        keys = pygame.key.get_pressed()
        
        #>player1
        if keys[pygame.K_w] and p1.rect.top > PADDING:
            p1.rect.y -= Player.SPEED
        if keys[pygame.K_s] and p1.rect.bottom < SCREEN_SIZE[1] - PADDING:
            p1.rect.y += Player.SPEED
            
        if keys[pygame.K_a] and p1.rect.left > PADDING:
            p1.rect.x -= Player.SPEED        
        if keys[pygame.K_d] and p1.rect.right < SCREEN_SIZE[0]/2 - PADDING:
            p1.rect.x += Player.SPEED
        
        #>player2 
        if keys[pygame.K_UP] and p2.rect.top > PADDING:
            p2.rect.y -= Player.SPEED
        if keys[pygame.K_DOWN] and p2.rect.bottom < SCREEN_SIZE[1] - PADDING:
            p2.rect.y += Player.SPEED
            
        if keys[pygame.K_LEFT] and p2.rect.left > SCREEN_SIZE[0]/2 + PADDING:
            p2.rect.x -= Player.SPEED        
        if keys[pygame.K_RIGHT] and p2.rect.right < SCREEN_SIZE[0]-PADDING:
            p2.rect.x += Player.SPEED

        #Display
        pygame.draw.rect(screen, rect = net , color=(150,150,150))
        screen.blit(p1.image,p1.rect)
        screen.blit(p2.image,p2.rect)
        screen.blit(ball.image,ball)
        
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())