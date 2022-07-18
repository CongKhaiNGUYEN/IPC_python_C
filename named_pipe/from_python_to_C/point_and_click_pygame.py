import pygame as pg
import os

class Character:

    def __init__(self, speed, color):
        self.image = pg.Surface((10, 10))
        self.image.set_colorkey((12,34,56))
        self.image.fill((12,34,56))
        pg.draw.circle(self.image, color, (50, 50), 5)
        self.rect = self.image.get_rect()
        self.color = color

        self.pos = pg.Vector2(50, 50)
        self.set_target((50, 50))
        self.speed = speed

    def set_target(self, pos):
        self.target = pg.Vector2(pos)

    def draw(self,screen):
        screen.fill((0, 0, 0))
        pg.draw.circle(screen, self.color , (self.pos[0], self.pos[1]), 5)
        pg.display.update()

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move

        self.rect.topleft = list(int(v) for v in self.pos)

def main():
    pg.init()
    path= "MYFIFO2"
    os.mkfifo(path)
    quit = False
    screen = pg.display.set_mode((1000, 500))
    clock = pg.time.Clock()

    Unit = Character(1.5, pg.Color('white'))

    while not quit:
        fifo = open(path,"w")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 
            if event.type == pg.MOUSEBUTTONDOWN:
                Unit.set_target(pg.mouse.get_pos())
                tar = f"x={Unit.target[0]} y={Unit.target[1]}"
                fifo.write(tar)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    fifo.write('end')
                    fifo.close()
                    pg.quit()

        Unit.update()
        screen.fill((20, 20, 20))
        Unit.draw(screen)
        pg.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()