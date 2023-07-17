import pygame

# Set up the Pygame window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Draw Path Example")

# Calculate the center of the window
center_x = window_width // 2
center_y = window_height // 2

# Define the path of points
path = [(100, 100), (200, 300), (400, 200), (600, 400)]

# Calculate the coordinates of the points centered in the window
centered_path = [(center_x + x, center_y + y) for x, y in path]

# Set the color
point_color = (255, 0, 0)  # Red

# Clear the window
window.fill((255, 255, 255))  # White

# Draw the points
for point in centered_path:
    pygame.draw.circle(window, point_color, point, radius=3)

# Update the display
pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
