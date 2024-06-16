import pygame
import sys


class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.rectangles = []
        self.font = pygame.font.SysFont(None, 24)
        self.setup_rectangles()

        # Text box attributes
        self.textbox_rect = pygame.Rect(50, self.screen.get_height() - 100, 300, 50)
        self.text_input = "undefined nickname"
        self.active_textbox = False

    def setup_rectangles(self):
        # Calculate rectangle positions based on number of options
        total_height = len(self.options) * 80
        y_offset = (self.screen.get_height() - total_height) // 2
        for i, option in enumerate(self.options):
            rect = pygame.Rect(50, y_offset + i * 80, 300, 50)
            self.rectangles.append(rect)

    def draw(self):
        self.screen.fill((255, 255, 255))  # Clear the screen

        # Draw the options rectangles and text
        for i, (rect, option) in enumerate(zip(self.rectangles, self.options)):
            # Change color if hovered over
            color = (0, 255, 0) if rect.collidepoint(pygame.mouse.get_pos()) else (0, 0, 255)
            pygame.draw.rect(self.screen, color, rect)

            # Draw text on rectangle
            text_surface = self.font.render(option[0], True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)

        # Draw the text box
        pygame.draw.rect(self.screen, (0, 0, 0), self.textbox_rect, 2)
        text_surface = self.font.render(self.text_input, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.textbox_rect.x + 5, self.textbox_rect.y + 15))

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
                # Check if the text box was clicked
                if self.textbox_rect.collidepoint(event.pos):
                    self.active_textbox = True
                else:
                    self.active_textbox = False
            elif event.type == pygame.KEYDOWN:
                if self.active_textbox:
                    if event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Handle Enter key press if needed
                        pass
                    else:
                        self.text_input += event.unicode

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            pygame.display.flip()
