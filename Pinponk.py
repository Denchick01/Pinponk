from pygame import *
class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed, vertekalno, horizontal):
                super().__init__()
                self.image = transform.scale(image.load(player_image),(vertekalno, horizontal))
                self.speed = player_speed
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
        def reset(self):
                window.blit(self.image, (self.rect.x, self.rect.y))          
class Player(GameSprite):
        def update(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_w] and self.rect.y > 5:
                        self.rect.y -= 10
                if keys_pressed[K_s] and self.rect.y < 395:
                        self.rect.y += 10
class Enemy (GameSprite):
        def update(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_UP] and self.rect.y > 5:
                        self.rect.y -= 10
                if keys_pressed[K_DOWN] and self.rect.y < 395:
                        self.rect.y += 10


#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("fomr.jpg"),(700, 500))
player = Player('ctena.jpeg', 0, 150, 15, 25, 100)
Enemy = Enemy('ctena.jpeg', 675, 150, 15, 25, 100)
ball = Player('merch.png', 330, 240, 10, 65, 65)

            
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
comput = 0
compute = 0
finish = player == ball
speed_x = 5
speed_y = 5
i = 0
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player, ball):
            speed_x *= -1
        if sprite.collide_rect(Enemy, ball): 
            speed_x *= -1
        if ball.rect.x >= 700:
            ball.rect.x = 350
            comput = comput + 1
        if ball.rect.x <= 0:
            ball.rect.x = 350
            compute = compute + 1
        schet1 = font.render(str(comput), True, (255, 215, 0))
        schet2 = font.render(str(compute), True, (255, 215, 0))   
        window.blit(schet1, (240, 0))
        window.blit(schet2, (450, 0))
        player.reset()
        player.update()
        Enemy.reset()
        Enemy.update()
        ball.reset()
        



    for e in event.get():
        if e.type == QUIT:
            game = False
        

    clock.tick(FPS)
    display.update()