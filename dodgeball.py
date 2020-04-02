

import pygame


pygame.init()
win = pygame.display.set_mode ((830, 467))
pygame.display.set_caption(("dodgeball"))

walkRight = [pygame.image.load('Run__000.png'), pygame.image.load('Run__001.png'), pygame.image.load('Run__002.png'), pygame.image.load('Run__003.png'), pygame.image.load('Run__004.png'), pygame.image.load('Run__005.png'), pygame.image.load('Run__006.png'), pygame.image.load('Run__007.png'), pygame.image.load('Run__008.png'), pygame.image.load('Run__009.png')]
walkLeft = [pygame.image.load('RunLeft__000.png'), pygame.image.load('RunLeft__001.png'), pygame.image.load('RunLeft__002.png'),pygame.image.load('RunLeft__003.png'), pygame.image.load('RunLeft__004.png'), pygame.image.load('RunLeft__005.png'), pygame.image.load('RunLeft__006.png'), pygame.image.load('RunLeft__007.png'), pygame.image.load('RunLeft__008.png'), pygame.image.load('RunLeft__009.png')]
slideRight= [pygame.image.load('Slide__000.png'), pygame.image.load('Slide__001.png'), pygame.image.load('Slide__002.png'), pygame.image.load('Slide__003.png'), pygame.image.load('Slide__004.png'), pygame.image.load('Slide__005.png'), pygame.image.load('Slide__006.png'), pygame.image.load('Slide__007.png'), pygame.image.load('Slide__008.png'), pygame.image.load('Slide__009.png')]
slideLeft= [pygame.image.load('SlideLeft__000.png'),pygame.image.load('SlideLeft__001.png'), pygame.image.load('SlideLeft__002.png'), pygame.image.load('SlideLeft__003.png'), pygame.image.load('SlideLeft__004.png'), pygame.image.load('SlideLeft__005.png'), pygame.image.load('SlideLeft__006.png'), pygame.image.load('SlideLeft__007.png'), pygame.image.load('SlideLeft__008.png'), pygame.image.load('SlideLeft__009.png')]
jumpRight= [pygame.image.load('Jump__000.png'), pygame.image.load('Jump__001.png'), pygame.image.load('Jump__002.png'), pygame.image.load('Jump__003.png'), pygame.image.load('Jump__004.png'), pygame.image.load('Jump__005.png'), pygame.image.load('Jump__006.png'), pygame.image.load('Jump__007.png'), pygame.image.load('Jump__008.png'), pygame.image.load('Jump__009.png')]
jumpLeft= [pygame.image.load('JumpLeft__000.png'), pygame.image.load('JumpLeft__001.png'), pygame.image.load('JumpLeft__002.png'), pygame.image.load('JumpLeft__003.png'), pygame.image.load('JumpLeft__004.png'), pygame.image.load('JumpLeft__005.png'), pygame.image.load('JumpLeft__006.png'), pygame.image.load('JumpLeft__007.png'), pygame.image.load('JumpLeft__008.png'), pygame.image.load('JumpLeft__009.png')]
Idle= [pygame.image.load('Idle__000.png'), pygame.image.load('Idle__001.png'), pygame.image.load('Idle__002.png'), pygame.image.load('Idle__003.png'), pygame.image.load('Idle__004.png'), pygame.image.load('Idle__005.png'), pygame.image.load('Idle__006.png'), pygame.image.load('Idle__007.png'), pygame.image.load('Idle__008.png'), pygame.image.load('Idle__009.png')]



ball= pygame.image.load('ball.png')






bg = pygame.image.load('Battleground3.png')


clock = pygame.time.Clock()
music= pygame.mixer.music.load('gamemain.mp3')
pygame.mixer.music.play(-1)





class ninja(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y= y
        self.width= width
        self.height= height
        self.vel = 10
        self.isJump = False
        self.jumpCount= 10
        self.left= False
        self.right= False
        self.walkCount= 0
        self.standing= True
        self.hitbox= (self.x, self.y, 60, 80)
        
        self.Right= False
        self.Left= False
        self.facing= facing
        self.slideCount= 10
        self.isSlide= False

    def draw(self,win):
        
        if self.walkCount + 1>= 20:
            self.walkCount = 0
        if self.standing:
            win.blit (Idle[0], (self.x, self.y))
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            
            elif self.Left:
                win.blit(slideLeft[self.slideCount//2], (self.x,self.y))
                self.slideCount += 1
            elif self.Right:
                win.blit(slideRight[self.slideCount//2], (self.x,self.y))
                self.slideCount += 1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                    
                elif self.left:
                    win.blit (walkLeft[0], (self.x, self.y))
                elif self.Right:
                    win.blit (slideRight[0], (self.x, self.y))
                elif self.Left:
                    win.blit (slideLeft[0], (self.x, self.y))
                
                

                    
        self.hitbox= (self.x, self.y, 60, 80)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

        if self.slideCount + 1>= 20:
            self.slideCount = 0
            
    
    
     

    def hit(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('You lose', 1, (255,0,0))
        win.blit(text, (300, 300))
        run= False
        pygame.display.update()
        i= 0
        while i< 300:
            pygame.time.delay(10)
            i += 1
        
            
        








class dodgeball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y= y
        self.radius= radius
        self.color= color
        self.direction= player.x, player.y
        self.xvel= 5
        self.yvel= 5
        self.hitbox= (self.x-20, self.y-20,40, 40)
        #pygame.draw.rect(win, (0,0,0), self.hitbox,2)

    def draw(self,win):
        self.hitbox= (self.x-20, self.y-20,40, 40)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        #pygame.draw.rect(win, (0,0,0), self.hitbox,2)
        self.x += self.xvel
        self.y += self.yvel
        pygame.display.update()

        
        
       





def GameWindow():
    
    win.blit(bg, (0,0))
    player.draw(win)
    ball.draw(win)

    pygame.display.update()
    
lasttime1= 0
lasttime2= 0
timediff= lasttime2 - lasttime1
dash= False

player= ninja(300, 250, 64, 64, 0)
ball= dodgeball(200,50, 20, (255,0,0))
font1 = pygame.font.SysFont('comicsans', 100)
run= True
while run== True:
    
    clock.tick(30)
    



   
    
    if ((ball.hitbox[0]+ ball.hitbox[2] >= player.hitbox[0] and ball.hitbox[0] + ball.hitbox[2] <= player.hitbox[0] + player.hitbox[2]) and ((ball.hitbox[1] <= player.hitbox[1] + player.hitbox[3] and ball.hitbox[1] >= player.hitbox[1]) or (ball.hitbox[1] + ball.hitbox[3] >= player.hitbox[1] and ball.hitbox[1] + ball.hitbox[3] <= player.hitbox[3]))) or ((ball.hitbox[1] + ball.hitbox[3]>= player.hitbox[1] and ball.hitbox[1] + ball.hitbox[3] <= player.hitbox[1] + player.hitbox[3]) and ((ball.hitbox[0] + ball.hitbox[2] >= player.hitbox[0] and ball.hitbox[0] + ball.hitbox[2]<= player.hitbox[0] + player.hitbox[2]) or (ball.hitbox[0]<= player.hitbox[0] + player.hitbox[2] and ball.hitbox[0] >= player.hitbox[0]))) or ((ball.hitbox[0] <= player.hitbox[0] + player.hitbox[2] and ball.hitbox[0] >= player.hitbox[0]) and ((ball.hitbox[1] + ball.hitbox[3] >= player.hitbox[1] and ball.hitbox[1] + ball.hitbox[3] <= player.hitbox[1] + player.hitbox[3]) or (ball.hitbox[1] >= player.hitbox[1] and ball.hitbox[1] <= player.hitbox[1] + player.hitbox[3]))) or ((ball.hitbox[1] <= player.hitbox[1] + player.hitbox[3] and ball.hitbox[1] >= player.hitbox[1]) and ((ball.hitbox[0] >= player.hitbox[0] and ball.hitbox[0] <= player.hitbox[0] + player.hitbox[2]) or (ball.hitbox[0] + ball.hitbox[2] >= player.hitbox[0] and ball.hitbox[0] + ball.hitbox[2] <= player.hitbox[0] + player.hitbox[2]))):
        print ("hit")
        player.hit()
        run= False

    if ball.x>=player.x and ball.y< player.y:
        ball.xvel = -5
        ball.yvel= 5
    elif ball.x<player.x and ball.y>player.y:
        ball.xvel= 5
        ball.yvel= -5
    elif ball.x<player.x and ball.y<player.y:
        ball.xvel= 5
        ball.yvel=5
    elif ball.x> player.x and ball.y >player.y:
        ball.xvel= -5
        ball.yvel= -5

    
   
        

   
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False


    keys= pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and (player.x<830 - player.width - player.vel):
        player.x += player.vel
        player.facing= 1
        player.right= True
        player.left= False
        player.standing= False
    elif keys[pygame.K_LEFT] and player.x> player.vel:
        player.x -= player.vel
        player.facing = -1
        player.left = True
        player.right= False
        player.standing= False
    else:
        player.standing= True
        player.walkCount= 0

    if not (player.isJump):
    
     
        if keys[pygame.K_UP] and player.y> player.vel:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y< 467- player.height - player.vel:
            player.y += player.vel
            
    else:
    
          
          
            if player.jumpCount >= -10:
                
                neg = 1
                if player.jumpCount< 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg
                player.jumpCount -= 1

            else:
                player.isJump= False
                player.jumpCount = 10
                
    
        
    if keys[pygame.K_SPACE]:
     
        gettime= pygame.time.get_ticks()
        lasttime2 = gettime
        timediff= lasttime2 - lasttime1
        if timediff >= 15000:
            
            lasttime1 = gettime
            
            for gettime in range (gettime, gettime + 10):
                
                if player.facing == 1 and player.x< 830 - player.width - player.vel:
                    
                
                    player.isJump = False
                    player.right= False
                    player.left= False
                    player.Right = True
                    player.Left = False
                    player.isSlide= True
                    player.x += 15
                    
                elif player.facing == -1 and player.x> player.vel:
                    
                    player.isJump = False
                    player.right= False
                    player.left= False
                    player.Left= True
                    player.Right= False
                    player.isSlide= True
                    player.x -= 15
                    
                else:
                    player.standing= True
                    player.slideCount= 0
            
                
      
    
    
            
      
       
        
            
           

    GameWindow()
    


    
        






    



    








