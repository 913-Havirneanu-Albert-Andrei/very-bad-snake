import pygame
import random
import sys
width , height = 900 , 500
wind = pygame.display.set_mode((width , height))
black = (0 , 0 , 0)
red = (255 , 0 , 0)
white = (255 , 255 , 255)
fps = 15


class Apple:
    def __init__(self):
        self._x = random.randint(1 , 88) * 10
        self._y = random.randint(1 , 48) * 10

    def change_coords(self):
        self._x = random.randint(1 , 88) * 10
        self._y = random.randint(1 , 48) * 10

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def show(self):
        pygame.draw.rect(wind , white , pygame.Rect(self._x , self._y , 20  ,20))

class Cell:
    def __init__(self , x , y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self , value):
        self._x = value

    @y.setter
    def y(self , value):
        self._y = value

    def __str__(self):
        return f"{self.x} , {self.y}"

    def __eq__(self , other):
        return self.x == other.x and self.y == other.y



class Snake:
    def __init__(self):
        self._head = Cell(420  , 220)
        self._snake = [self._head]
        self.dir = ''

    @property
    def head(self):
        return self._head

    def dead(self):
        if self._head.x > 880 or self._head.y > 480 or self._head.x < 5 or self._head.y < 5:
            return True
        for i in range(len(self._snake) - 1):
            for j in range(i + 1 , len(self._snake)):
                if self._snake[i] == self._snake[j]:
                    return True
        return False

    def show(self):
        pygame.draw.rect(wind , (0 , 255 , 0) ,pygame.Rect(self._snake[0].x , self._snake[0].y , 20 , 20))
        for s in self._snake[1:]:
            pygame.draw.rect(wind , red , pygame.Rect(s.x , s.y , 20 , 20))

    def move_right(self):
        self.dir = 'r'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x - 10
            self._snake[i].y = self._snake[i - 1].y
        self._snake[0].x += 10

    def move_down(self):
        self.dir = 'd'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x
            self._snake[i].y = self._snake[i - 1].y - 10
        self._snake[0].y += 10


    def move_up(self):
        self.dir = 'u'
        for i in range(len(self._snake) - 1, 0, -1):
            self._snake[i].x = self._snake[i - 1].x
            self._snake[i].y = self._snake[i - 1].y + 10
        self._snake[0].y -= 10

    def move_left(self):
        self.dir = 'l'
        for i in range(len(self._snake) - 1 , 0 , -1):
            self._snake[i].x = self._snake[i - 1].x + 10
            self._snake[i].y = self._snake[i - 1].y
        self._snake[0].x -= 10

    def add_cell(self):
        x_new = None
        y_new = None
        if self.dir == 'r':
            x_new = self._snake[-1].x - 20
            y_new = self._snake[-1].y
        if self.dir == 'l':
            x_new = self._snake[-1].x + 20
            y_new = self._snake[-1].y
        if self.dir == 'u':
            x_new = self._snake[-1].x
            y_new = self._snake[-1].y + 20
        if self.dir == 'd':
            x_new = self._snake[-1].x
            y_new = self._snake[-1].y - 20
        new_cell = Cell(x_new, y_new)
        self._snake.append(new_cell)

if __name__ == "__main__":
    run = True
    snake = Snake()
    apple = Apple()
    move_down = False
    move_up = False
    move_right = False
    move_left = False
    clock = pygame.time.Clock()
    while run:
        clock.tick(fps)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_d:
                    if move_left == True:
                        sys.exit()
                    move_right = True
                    move_left = move_up = move_down = False
                if ev.key == pygame.K_s:
                    if move_up == True:
                        sys.exit()
                    move_down = True
                    move_left = move_up = move_right = False
                if ev.key == pygame.K_w:
                    if move_down == True:
                        sys.exit()
                    move_up = True
                    move_left = move_right = move_down = False
                if ev.key == pygame.K_a:
                    if move_right == True:
                        sys.exit()
                    move_left = True
                    move_right = move_down = move_up = False

        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.add_cell()
            apple.change_coords()

        if snake.dead():
            run = False
            print("u ded")

        if move_right == True:
            snake.move_right()

        if move_down == True:
            snake.move_down()
            print(snake.dir)

        if move_up == True:
            snake.move_up()
            print(snake.dir)

        if move_left == True:
            snake.move_left()
            print(snake.dir)

        snake.show()
        apple.show()
        pygame.display.update()
        wind.fill(black)


