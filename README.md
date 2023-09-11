# Fractals
Fractal App

IN PROGRESS

Currently making a usable menu to swap between fractal patterns, also figuring out math for sierpinski's triangle

## Program usage
To run the program, open a terminal window and type 'cd' followed by a space and the filepath of the folder that snowflake.py or snowflakeFAT.py.
Please ensure that you have python installed and the python library pygame installed as well.
Type 'python snowflake.py' or 'python snowflakeFAT.py' depending on the program you would like to use. A window should appear saying "Generating fractal pattern orders 1 - 10", after the window changes and displays a triangle with 3 buttons at the bottom. You can use the program
The program starts with displaying the first order of the koch snowflake, an equilateral triangle.
The user can interact with the program by pressing the buttons specified below or resizing the window.
The buttons include:

Red button: to decrease the pattern order by 1 to be displayed. It cannot go below order 1
Yellow button: to reset the pattern order and start at order 1 again.
Green button: to increase the pattern order by 1 to be displayed. It cannot go over 10.

The current pattern order will be displayed on top of the window e.g "Koch Snowflake order: 2".
*Note that for order 10, there will be a slight delay when drawing the pattern. As for resizing on order 10, the window will go black for abit before the resized order 10 is drawn on the window
