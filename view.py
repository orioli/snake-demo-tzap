import pygame

class SnakeGameView:
    def __init__(self):
        self.window_width = 800  # Adjust window width as needed
        self.window_height = 600  # Adjust window height as needed
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("(TZAP.IO)")

    def render(self, snake):
        self.window.fill((0, 0, 0))  # Fill the window with black color

        # Render the snake
        for segment in snake.body:
            pygame.draw.rect(self.window, (0, 255, 0), (segment[0], segment[1], 10, 10))

        pygame.display.update()