import sys
from Snake import Snake
from Apple import Apple
from Constants import *


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


