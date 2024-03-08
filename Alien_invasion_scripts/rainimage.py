import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display Resized Image")

# Load the original image
original_image_path = "images/raindrop.bmp"
original_image = pygame.image.load(original_image_path)

# Define the desired width and height for the resized image
desired_width = 100
desired_height = 100

# Resize the image
resized_image = pygame.transform.scale(original_image, (desired_width, desired_height))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white background

    # Blit the resized image onto the screen at position (0, 0)
    screen.blit(resized_image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
