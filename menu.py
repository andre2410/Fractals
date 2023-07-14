import pygame
import pygame_menu
import snowflake
import sys

# Main file for running Koch Snowflake menu
# Author: Andrew Goh

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Fractals")

# Colors
blue = (0, 0, 255)
white = (255, 255, 255)


def main():
    # Game loop
    try:
        # Create the menu
        menu = pygame_menu.Menu("Fractal Patterns", 400, 300, theme=pygame_menu.themes.THEME_BLUE)

        # Add menu items
        menu.add.button("Koch Snowflake", lambda: print("launching snowflake"))
        menu.add.button("Sierpinski Triangle", lambda: print("launching triangle"))
        menu.add.button("Mandelbrot Set", lambda: print("launching mandelbrot"))
        menu.add.button("Quit", pygame_menu.events.EXIT)

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill(white)

            # Update and draw the menu
            menu.update(pygame.event.get())
            menu.draw(screen)

            # Update the display
            pygame.display.flip()

        # Quit menu
        pygame.quit()
        sys.exit()
    except(KeyboardInterrupt):
        print("bye")

#Run program
main()
