# Name: Elmer Rodriguez
# Institution: University of Rochester
# Professor: Richard Sarkis
# Course: CSC 161: INTRO TO PROGRAMMING
# Assignment: Numbers
# All Rights Reserved

#filename:

"""
Description

Program that allows the user to draw a simple house using five mouse clicks.

Click 1 and 2 will mark the opposite corners of the rectangular frame of the house.
Click 3 will indicate the center of the top edge of a rectangular door. The door should have a total width that is 1515 of the width of the house frame. The sides of the door should extend from the corners of the top all the way down to the bottom of the frame.
Click 4 will indicate the center of a square window. The window is 3434 as wide as the door.
Click 5, the last click, will indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.

"""

# importing "graphics.py" module
import graphics


def main():

    # creating a graphics window
    window = graphics.GraphWin("Objects and Graphics: Making a House", 600, 600)

    # drawing the frame
    click1 = window.getMouse()
    click2 = window.getMouse()
    frame = graphics.Rectangle(click1, click2)
    frame.draw(window)

    # drawing the door
    click3 = window.getMouse()

    houseWidth = click1.getX() - click2.getX()
    doorWidth = houseWidth / 5

    doorBottomRightX = click3.getX() - doorWidth / 2
    doorBottomRightY = click1.getY()
    doorBottomRight = graphics.Point(doorBottomRightX, doorBottomRightY)

    doorTopLeftX = click3.getX() + doorWidth / 2
    doorTopLeftY = click3.getY()
    doorTopLeft = graphics.Point(doorTopLeftX, doorTopLeftY)

    door = graphics.Rectangle(doorBottomRight, doorTopLeft)
    door.draw(window)

    # drawing an actual window in the house
    click4 = window.getMouse()
    fenetreWidth = doorWidth * 3 / 4

    BottomLeftX = click4.getX() - fenetreWidth / 2
    fenetreBottomLeftY = click4.getY() + fenetreWidth / 2
    fenetreBottomLeft = graphics.Point(fenetreBottomLeftX,
                                       fenetreBottomLeftY)

    fenetreTopRightX = click4.getX() + fenetreWidth / 2
    fenetreTopRightY = click4.getY() - fenetreWidth / 2
    fenetreTopRight = graphics.Point(fenetreTopRightX, fenetreTopRightY)

    fenetre = graphics.Rectangle(fenetreBottomLeft, fenetreTopRight)
    fenetre.draw(window)

    # drawing the roof
    click5 = window.getMouse()
    rightSide = graphics.Line(graphics.Point(click1.getX(), click2.getY()),
                              click5)
    leftSide = graphics.Line(click5, click2)

    rightSide.draw(window)
    leftSide.draw(window)

    window.getMouse()

# calling main
main()