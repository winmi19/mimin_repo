import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 游戏常量
WIDTH = 800
HEIGHT = 600


#颜色设置
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#字体设置
font = pygame.font.SysFont('comicsans', 30)

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("使用类和精灵组绘制正方形")
clock = pygame.time.Clock()

class Coin(pygame.sprite.Sprite):
    def __init__(self,size=40):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.size = size
        self.randomize_position()
        self.speed=3

    #随机产生金币
    def randomize_position(self):
        self.rect.x=random.randint(0,WIDTH-self.size)
        self.rect.y=-self.size

    #移动
    def update(self):
        self.rect.y += self.speed



class Player(pygame.sprite.Sprite):
    def __init__(self,size=50):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.speed=6
        self.rect.x=WIDTH//2
        self.rect.y=HEIGHT-80
        self.size = size

    #用户输入判断 向左向右移动
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif key[pygame.K_RIGHT] and self.rect.x+self.size < WIDTH:
            self.rect.x += self.speed




def main():
    all_sprites = pygame.sprite.Group()
    player=Player()
    all_sprites.add(player)

    coin_group = pygame.sprite.Group()
    #创建3个金币
    for _ in range(3):
        coin=Coin()
        all_sprites.add(coin)
        coin_group.add(coin)

    count=0
    game_over=False
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        if not game_over:
            all_sprites.update()

            coin_hits=pygame.sprite.spritecollide(player,coin_group,True)
            #碰撞后删除

            for hit in coin_hits:
                coin=Coin()
                all_sprites.add(coin)
                coin_group.add(coin)
                count+=5

            #判断游戏结束代码
            if count==50:
                game_over=True

            screen.fill(BLACK)
            all_sprites.draw(screen)
            clock.tick(20)

            #显示当前分数
            meg=font.render(f"count:{count}",True,RED)
            screen.blit(meg,(10,10))

        if game_over:
            text=font.render("GAME OVER", True, WHITE)
            screen.blit(text,(WIDTH//2,HEIGHT//2))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()







