
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Diamond Shape")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Function to draw a diamond
def draw_diamond(surface, color, center, size):
    x, y = center
    points = [
        (x, y - size),  # Top
        (x + size, y),  # Right
        (x, y + size),  # Bottom
        (x - size, y)   # Left
    ]
    pygame.draw.polygon(surface, color, points)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the diamond
    draw_diamond(screen, BLUE, (width // 2, height // 2), 100)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()