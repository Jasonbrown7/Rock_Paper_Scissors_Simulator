import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (1000, 800)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Bouncing Balls')

# Set the colors for the balls
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Set the initial positions and velocities for the balls
balls = []
for color in colors:
    for i in range(5):
        if color == (255, 0, 0):  # Red balls
            x = random.randint(window_size[0] - 300, window_size[0] - 20)  # Top right
            y = random.randint(1, 350)  # Top right
        elif color == (0, 255, 0):  # Green balls
            x = random.randint((window_size[0] / 2) - 200, (window_size[0] / 2) + 200)  # Bottom center
            y = random.randint(450, 780)
        else:  # Blue balls
            x = random.randint(20, 350)   # Top left
            y = random.randint(1, 350)
        vx = random.uniform(-3, 3)
        vy = random.uniform(-3, 3)
        balls.append((x, y, vx, vy, color))

# Set the radius of the balls
radius = 20

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the positions of the balls
    for i in range(len(balls)):
        x, y, vx, vy, color = balls[i]
        x += vx
        y += vy
        if x < radius or x > window_size[0] - radius:
            vx = -vx
        if y < radius or y > window_size[1] - radius:
            vy = -vy
        balls[i] = (x, y, vx, vy, color)
    
    # Check for collisions between the balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            x1, y1, vx1, vy1, color1 = balls[i]
            x2, y2, vx2, vy2, color2 = balls[j]
            dx = x2 - x1
            dy = y2 - y1
            d = (dx**2 + dy**2)**0.5
            if d < (2 * radius)-1:
                # Update the colors of the balls that are involved in the collision
                if color1 == (0, 255, 0) and color2 == (0, 0, 255):
                    color2 = (0, 255, 0)
                elif color1 == (0, 0, 255) and color2 == (255, 0, 0):
                    color2 = (0, 0, 255)
                elif color1 == (255, 0, 0) and color2 == (0, 255, 0):
                    color2 = (255, 0, 0)
                vx1, vy1, vx2, vy2 = vx2, vy2, vx1, vy1
                balls[i] = (x1, y1, vx1, vy1, color1)
                balls[j] = (x2, y2, vx2, vy2, color2)
    
    # Clear the screen
    screen.fill((225, 225, 225)) 
    
    # Draw the balls
    for x, y, vx, vy, color in balls:
        pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()