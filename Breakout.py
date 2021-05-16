import pygame
import random
import time
pygame.init()

class Color:
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    yellow = (255,255,0)
class Brick:
    def __init__(self):
        self.w = 40
        self.h = 10
        self.x = 5 
        self.y = 30
        self.color = Color.blue
        self.block = []
        for j in range(0,4):
            for i in range(0,int(Game.width/self.w)):
                self.block.append(pygame.draw.rect(Game.screen,self.color,[self.x + i*50,self.y + j*15,self.w,self.h]))
            
    def show(self):
        for brick in self.block:
            self.area=pygame.draw.rect(Game.screen,self.color,brick)

class Rocket:
    def __init__(self , x, y , color):
        self.w = 80
        self.h = 10
        self.x = x
        self.y = y
        self.color = color
        self.speed = 10
        self.score = 0
        self.x_dir = 0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x  , self.y , self.w , self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x , self.y , self.w , self.h])
    def move(self):
        if self.x_dir == 1 :
            self.x += self.speed
            if self.x > Game.width - 80:
                self.x = Game.width - 80
        if self.x_dir == -1:
            self.x -= self.speed
            if self.x < 0 :
                self.x = 0

class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width/2
        self.y = Game.height/2
        self.speed = 6
        self.color = Color.yellow
        self.x_direction = int(random.choice([1,-1]))
        self.y_direction = int(random.choice([1,-1]))
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x ,self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x,self.y], self.r)

    def move(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction

        if self.x > Game.width or self.x <0:
            self.x_direction *= -1
    def new(self):
        self.x = Game.width/2
        self.y = Game.height/2

class Game:
    width = 400
    height = 700
    screen = pygame.display.set_mode((width , height))
    pygame.display.set_caption("Breakout")
    clock = pygame.time.Clock()
    fps = 30
    balls = 3
    score = 0

    @staticmethod
    def play():
        pygame.mouse.set_visible(False)
        me = Rocket(Game.width/2, Game.height - 50, Color.red)
        ball = Ball()
        brick = Brick()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                me.y = Game.height - me.h
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        me.x_dir = -1
                    elif event.key == pygame.K_e:
                        me.x_dir = 1
            Game.screen.fill(Color.black)

            if ball.y > Game.height  :
                Game.balls -= 1
                if Game.balls > 0:
                    ball.new()
                else:
                    Game.balls = 0
            if me.area.collidepoint(ball.x,ball.y):
                ball.y_direction *= -1
            if ball.y < 5:
                ball.y_direction *= -1

            for block in brick.block:
                if ball.area.colliderect(block):
                    ball.x_direction*=1
                    ball.y_direction*=-1
                    brick.block.remove(block)
                    Game.score += 1
            font = pygame.font.SysFont('Arial', 15)
            text_me=font.render('Score = '+str(Game.score),True,(125,0,125))
            text_ball = font.render('Ball = '+str(Game.balls),True,(125,0,125))
            Game.screen.blit(text_me,(15,5))
            Game.screen.blit(text_ball,(320,5))
            if Game.balls == 0 :
                text_Gameover = font.render('Game Over!!!' , True,(255,0,0))
                Game.screen.blit(text_Gameover,(150,Game.height/2))
                time.sleep(5)
                pygame.display.update()
                break
            ball.move()
            me.move()
            me.show()
            ball.show()
            brick.show()
            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()