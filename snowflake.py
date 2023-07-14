import pygame
from math import sin, cos, pi
# Functions for Koch Snowflake fractal pattern
# Author: Andrew Goh

# Init pygame resources
pygame.init()
#Set variables needed for program
#width and height of 
width = 640
height = 480
windowWidth = 600
windowHeight = 650
#Pygame window variables
window = None
renderer = None
renderer = None
button1 = None
button2 = None
button3 = None
quit = False
# Current order number to be displayed
order = 1
#list needed for curve drawing
orders = []
lines = []

#Class Line for each line
class Line:
    def __init__(self, x, y, length, angle):
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle
        self.ex = self.x + cos(self.angle * (pi / 180.0)) * self.length
        self.ey = self.y + sin(self.angle * (pi / 180.0)) * self.length
    #Function to draw line
    def draw(self):
        global prevx
        #new scaled x and y
        sx = renderer.get_width() / 600
        sy = renderer.get_height() / 650
        #scale to be used
        scale = min(sx, sy)
        #end values
        px = ((self.x *scale), (self.y *scale))
        py = ((self.ex *scale), (self.ey * scale))
        #draw line
        pygame.draw.line(renderer, (0, 0, 255), px, py, 1)
        prevx = sx
    def toString(self):
        print("x: " + str(self.x))
        print("y: " + str(self.y))
        print("length: " + str(self.length))
        print("angle: " + str(self.angle) + "\n")

#Function for displaying start window
def displayStart():
    global window
    #Create the window
    window = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Koch Snowflake")
    #Create a font object
    font = pygame.font.SysFont(None, 30)
    # Render text
    text = font.render("Generating fractal orders 1 - 10", True, (0, 0, 255))
    #Center the text in the window
    text_rect = text.get_rect(center=(400 // 2, 200 // 2))
    #Fill the window with a black background
    window.fill((255, 255, 255))
    #Add the text onto the window
    window.blit(text, text_rect)
    # Update the display
    pygame.display.flip()

#Function for displaying main window for koch snowflake interaction
def displayWindow():
    global button1, button2, button3, renderer, window
    #Display pygame Window
    window = pygame.display.set_mode((windowWidth, windowHeight), pygame.RESIZABLE)
    pygame.display.set_caption("Koch Snowflake: order " + str(order))
    #Create surface
    renderer = pygame.Surface(window.get_size())
    renderer = renderer.convert()
    #recalculate button size
    buttonWidth = windowWidth / 3
    buttonHeight = windowHeight / 3
    button1 = pygame.Rect(0, windowHeight-100, buttonWidth, buttonHeight)
    button2 = pygame.Rect((windowWidth/3) , windowHeight-100, buttonWidth, buttonHeight)
    button3 = pygame.Rect((windowWidth/3) * 2, windowHeight-100, buttonWidth, buttonHeight)
    #recalculate window
    if (windowWidth != 600) or (windowHeight != 650):
        x = (windowWidth - renderer.get_width()) // 2
        y = (windowHeight - renderer.get_height()) // 2
        window.fill((255,255,255))
        window.blit(renderer, (x,y))
        pygame.display.flip()

#Important function for generating koch snowflake lines
def koch_snowflake(lines):
    print("Generating snowflake orders 1-10")
    global orders, order
    #Loop and create lines
    for j in range(0, 10):
        #append order to orders
        if (j != 0): orders.append(lines)
        #break once last order is added to orders
        if j == 10: break
        #array of new lines
        new_lines = []
        #Create 4 new lines for each line
        for line in lines:
            #First line
            l1_x = line.x
            l1_y = line.y
            l1_len = line.length / 3.0
            l1_angle = line.angle
            l1 = Line(l1_x, l1_y, l1_len, l1_angle)
            #Second line
            l2_x = line.x + (cos(line.angle * (pi / 180.0)) * line.length / 3.0)
            l2_y = line.y + (sin(line.angle * (pi / 180.0)) * line.length / 3.0)
            l2_len = line.length / 3.0
            l2_angle = line.angle + 300.0
            l2 = Line(l2_x, l2_y, l2_len, l2_angle)
            #Third line
            l3_x = line.x + (cos(line.angle * (pi / 180.0)) * line.length / 1.5)
            l3_y = line.y + (sin(line.angle * (pi / 180.0)) * line.length / 1.5)
            l3_len = line.length / 3.0
            l3_angle = line.angle + 240
            #Flip drawing angle
            l3_x = l3_x + cos(l3_angle * (pi / 180)) * l3_len
            l3_y = l3_y + sin(l3_angle * (pi / 180)) * l3_len
            l3_angle += 180
            l3 = Line(l3_x, l3_y, l3_len, l3_angle)
            #Fourth line
            l4_x = line.x + (cos(line.angle * (pi / 180.0)) * line.length / 1.5)
            l4_y = line.y + (sin(line.angle * (pi / 180.0)) * line.length / 1.5)
            l4_len = line.length / 3.0
            l4_angle = line.angle
            l4 = Line(l4_x, l4_y, l4_len, l4_angle)
            #add 4 new lines to new_lines array
            new_lines.extend([l1, l2, l3, l4])
        lines = new_lines

#Function to draw snowflake order
def draw_snowflake(snowflake):
    for line in snowflake:
        line.draw()

#Function to draw current renderer surface to window
def draw_order():
    # global variables
    global renderer, window
    # fill renderer
    renderer.fill((255, 255, 255))
    # draw snowflake order
    draw_snowflake(orders[order-1])
    # draw buttons
    pygame.draw.rect(renderer, (255, 0, 0), button1)
    pygame.draw.rect(renderer, (255, 255, 0), button2)
    pygame.draw.rect(renderer, (0, 255, 0), button3)
    # display window
    x = (windowWidth - renderer.get_width()) // 2
    y = (windowHeight - renderer.get_height()) // 2
    window.fill((255, 255, 255))
    window.blit(renderer, (x, y))
    pygame.display.flip()

#Function to decrease order 
def decrease_order():
    global order
    # print(order)
    if order == 1:
        return
    order -= 1
    draw_order()

#Function to increase order
def increase_order():
    global order
    if order == 10:
        return
    order += 1
    draw_order()

#main method
def snowflake():
    try:
    #Global variables
        global windowWidth, windowHeight, quit, order
        #Display loading window
        displayStart()
        # Set equilateral triangle for base of snowflake
        #line 1
        line1 = Line(width - 100, 400, width - 200, 180)
        #line 2
        line2 = Line(100, 400, width - 200, 300)
        #line 3
        line3 = Line(width - 100, 400, width - 200, 240)
        #append first 3 lines
        lines.extend([line1, line2, line3])
        orders.append(lines)
        #create line 3 copy
        line4 = Line(width - 100, 400, width - 200, 240)
        #Fix line 3 angle for correct drawing
        line4.x = line4.x + cos(line4.angle * (pi / 180)) * line4.length
        line4.y = line4.y + sin(line4.angle * (pi / 180)) * line4.length
        line4.angle += 180
        #newlines to be parsed into koch_snowflake method
        newlines = []
        newlines.extend([line1, line2, line4])
        # Generate snowflake orders
        koch_snowflake(newlines)
        print("Launching snowflake app")
        displayWindow()
        draw_order()
        #While loop to run application
        while not quit:
            for event in pygame.event.get():
                #Change display to reflect order number 
                pygame.display.set_caption("Koch Snowflake: order " + str(order))
                #If handle quit event
                if event.type == pygame.QUIT:
                    quit = True
                #handle mouse button event
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #handles which buttons are pressed
                    if event.button == 1:
                        if button1.collidepoint(event.pos):
                            decrease_order()
                            continue
                        elif button2.collidepoint(event.pos):
                            order = 1
                            draw_order()
                            continue
                        elif button3.collidepoint(event.pos):
                            increase_order()
                            continue
                #handle resizing of window
                elif event.type == pygame.VIDEORESIZE:
                    #update size of window
                    windowWidth, windowHeight = event.w, event.h
                    #redraw window
                    displayWindow()
                    draw_order()
        #quit pygame once done to free resources
        pygame.quit()
    except(KeyboardInterrupt):
        print("bye")
