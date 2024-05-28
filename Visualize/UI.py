import pygame
from MapVisualize import elevation_map, plot_grid, plot_discretized_data
import pickle
import imageio.v3 as iio

file = ".//Mesh//discretized_data.pkl"
with open(file, 'rb') as f:
        X, Y, elevation, test_grid = pickle.load(f)

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
button_width = 300
button_height = 50

# Define button positions
button1_x = (screen_width - button_width) // 2
button1_y = (screen_height - button_height) // 2 - 200
button2_x = (screen_width - button_width) // 2
button2_y = (screen_height - button_height) // 2 + 200
button3_x = (screen_width - button_width) // 2
button3_y = (screen_height - button_height) // 2
'''
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
                elevation_map(test_grid)  # Call the elevation_map function from MapVisualize
            # Check if button 2 is clicked
            elif pygame.Rect(button2_x, button2_y, button_width, button_height).collidepoint(event.pos):
                plot_grid(X,Y,elevation)  # Call the plot_grid function from MapVisualize
            elif pygame.Rect(button3_x, button3_y, button_width, button_height).collidepoint(event.pos):
                plot_discretized_data(X,Y,elevation)

    # Clear the screen
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, GRAY, (button1_x, button1_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button2_x, button2_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button3_x, button3_y, button_width, button_height))

    # Draw button labels
    font = pygame.font.Font(None, 36)
    button1_label = font.render("Elevation map", True, BLACK)
    button2_label = font.render("Grid", True, BLACK)
    button3_label = font.render("Discretized Data", True, BLACK)
    screen.blit(button1_label, (button1_x + 30, button1_y + 10))
    screen.blit(button2_label, (button2_x + 30, button2_y + 10))
    screen.blit(button3_label, (button3_x + 30, button3_y + 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
'''

# Main menu loop
menu_running = True
while menu_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button 1 is clicked
            if pygame.Rect(button1_x, button1_y, button_width, button_height).collidepoint(event.pos):
                elevation_map(test_grid)  # Call the elevation_map function from MapVisualize
            # Check if button 2 is clicked
            elif pygame.Rect(button2_x, button2_y, button_width, button_height).collidepoint(event.pos):
                plot_grid(X,Y,elevation)  # Call the plot_grid function from MapVisualize
            elif pygame.Rect(button3_x, button3_y, button_width, button_height).collidepoint(event.pos):
                plot_discretized_data(X,Y,elevation)
                menu_running = False  # Exit the menu loop after displaying the figure

    # Clear the screen
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, GRAY, (button1_x, button1_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button2_x, button2_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button3_x, button3_y, button_width, button_height))

    # Draw button labels
    font = pygame.font.Font(None, 36)
    button1_label = font.render("Elevation map", True, BLACK)
    button2_label = font.render("Grid", True, BLACK)
    button3_label = font.render("Discretized Data", True, BLACK)
    screen.blit(button1_label, (button1_x + 30, button1_y + 10))
    screen.blit(button2_label, (button2_x + 30, button2_y + 10))
    screen.blit(button3_label, (button3_x + 30, button3_y + 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()