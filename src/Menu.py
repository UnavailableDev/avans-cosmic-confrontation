import pygame
import sys

from ScreenWrapper import ScreenWrapper


class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.rectangles = []
        self.font = pygame.font.SysFont(None, 24)
        self.setup_rectangles()

    def setup_rectangles(self):
        # Calculate rectangle positions based on number of options
        total_height = len(self.options) * 80
        y_offset = (self.screen.get_height() - total_height) // 2
        for i, option in enumerate(self.options):
            rect = pygame.Rect(50, y_offset + i * 80, 300, 50)
            self.rectangles.append(rect)

    def draw(self):
        self.screen.fill((255, 255, 255))  # Clear the screen
        for i, (rect, option) in enumerate(zip(self.rectangles, self.options)):
            # Change color if hovered over
            color = (0, 255, 0) if rect.collidepoint(pygame.mouse.get_pos()) else (0, 0, 255)
            pygame.draw.rect(self.screen, color, rect)

            # Draw text on rectangle
            text_surface = self.font.render(option[0], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a rectangle was clicked
                for i, rect in enumerate(self.rectangles):
                    if rect.collidepoint(event.pos):
                        # Call the associated function
                        self.options[i][1]()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            pygame.display.flip()


# Initialize Pygame
# pygame.init()

# # Create the screen
# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Menu Class Example")
