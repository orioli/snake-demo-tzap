import pygame
from model import Snake
from view import SnakeGameView

class SnakeGameController:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.view = SnakeGameView()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")

    def game_loop(self):
        while True:
            self.handle_events()
            self.snake.move()
            self.view.render(self.snake)
            pygame.time.delay(50)  # Adjust the delay as needed for desired game speed
