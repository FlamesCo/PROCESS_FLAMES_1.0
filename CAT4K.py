# Import the pygame module
import pygame

# Initialize all imported pygame modules
pygame.init()

# Set the dimensions of the window
win = pygame.display.set_mode((800, 600))

# Create a new Font object from a file
font = pygame.font.Font(None, 36)

# Render the text 'Hello Cat' with anti-aliasing and white color
text = font.render('Hello Cat', True, (255, 255, 255))

# Get the rectangular area of the Surface
text_rect = text.get_rect(center=(400, 300))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        # If the QUIT event is received, set running to False
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with black
    win.fill((0, 0, 0))

    # Draw the text surface onto another with the specified position
    win.blit(text, text_rect)

    # Update the full display Surface to the screen
    pygame.display.flip()

# Uninitialize all pygame modules that have previously been initialized
pygame.quit()