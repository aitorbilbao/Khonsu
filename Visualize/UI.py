import pygame
from MapVisualize import elevation_map, plot_grid

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Demo")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Define button dimensions
button_width = 200
button_height = 50

# Define button positions
button1_x = (screen_width - button_width) // 2
button1_y = (screen_height - button_height) // 2 - 100
button2_x = (screen_width - button_width) // 2
button2_y = (screen_height - button_height) // 2 + 100

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button 1 is clicked
            if pygame.Rect(button1_x, button1_y, button_width, button_height).collidepoint(event.pos):
                elevation_map()  # Call the elevation_map function from MapVisualize
            # Check if button 2 is clicked
            elif pygame.Rect(button2_x, button2_y, button_width, button_height).collidepoint(event.pos):
                plot_grid()  # Call the plot_grid function from MapVisualize

    # Clear the screen
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, GRAY, (button1_x, button1_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button2_x, button2_y, button_width, button_height))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()