import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Ball dimensions
BALL_RADIUS = 10

# Number of balls
NUM_BALLS = 4

# Lists to store ball data
red_positions = []
blue_positions = []
green_positions = []
red_speeds = []
blue_speeds = []
green_speeds = []

# Initial

# Initialize ball positions and speeds
for i in range(NUM_BALLS):
    red_positions.append([random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS), random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)])
    blue_positions.append([random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS), random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)])
    green_positions.append([random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS), random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)])
    red_speeds.append([random.randint(-5, 5), random.randint(-5, 5)])
    blue_speeds.append([random.randint(-5, 5), random.randint(-5, 5)])
    green_speeds.append([random.randint(-5, 5), random.randint(-5, 5)])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball positions
    for i in range(NUM_BALLS):
        red_positions[i][0] += red_speeds[i][0]
        red_positions[i][1] += red_speeds[i][1]
        blue_positions[i][0] += blue_speeds[i][0]
        blue_positions[i][1] += blue_speeds[i][1]
        green_positions[i][0] += green_speeds[i][0]
        green_positions[i][1] += green_speeds[i][1]

    # Check for ball-wall collisions and reverse direction if necessary
    for i in range(NUM_BALLS):
        if red_positions[i][0] - BALL_RADIUS < 0 or red_positions[i][0] + BALL_RADIUS > SCREEN_WIDTH:
            red_speeds[i][0] = -red_speeds[i][0]
        if red_positions[i][1] - BALL_RADIUS < 0 or red_positions[i][1] + BALL_RADIUS > SCREEN_HEIGHT:
            red_speeds[i][1] = -red_speeds[i][1]
        if blue_positions[i][0] - BALL_RADIUS < 0 or blue_positions[i][0] + BALL_RADIUS > SCREEN_WIDTH:
            blue_speeds[i][0] = -blue_speeds[i][0]
        if blue_positions[i][1] - BALL_RADIUS < 0 or blue_positions[i][1] + BALL_RADIUS > SCREEN_HEIGHT:
            blue_speeds[i][1] = -blue_speeds[i][1]
        if green_positions[i][0] - BALL_RADIUS < 0 or green_positions[i][0] + BALL_RADIUS > SCREEN_WIDTH:
            green_speeds[i][0] = -green_speeds[i][0]
        if green_positions[i][1] - BALL_RADIUS < 0 or green_positions[i][1] + BALL_RADIUS > SCREEN_HEIGHT:
            green_speeds[i][1] = -green_speeds[i][1]

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the balls
    for i in range(NUM_BALLS):
        pygame.draw.circle(screen, RED, red_positions[i], BALL_RADIUS)
        pygame.draw.circle(screen, BLUE, blue_positions[i], BALL_RADIUS)
        pygame.draw.circle(screen, GREEN, green_positions[i], BALL_RADIUS)

    # Update the display
    pygame.display.update()

    # Set frame rate
    pygame.time.delay(30)

# Quit pygame
pygame.quit()