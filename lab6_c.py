'''
This module simulates balls bouncing around a canvas.
'''

import math, random, time
from tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''

    def __init__(self, canvas, center, radius, color, direction, speed):
        '''
        Create a new ball with a given location, direction, color, and speed.

        Arguments:
          canvas:    the canvas the ball moves on
          center:    the center of the ball in (x, y) pixel coordinates
          radius:    the radius of the ball in pixels
          color:     the color of the ball
          direction: the initial direction the ball is moving
          speed:     the initial speed of the ball
        '''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0:
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''
        Move this ball in its current direction with its current speed.
        Change direction if the edge of the canvas is reached.

        Arguments: none
        Return value: none
        '''
        vx = self.speed * self.dirx
        vy = self.speed * self.diry
        dx = self.displacement(self.center[0], vx, self.xmax)
        if dx != vx:
            self.dirx *= -1
        dy = self.displacement(self.center[1], vy, self.ymax)
        if dy != vy:
            self.diry *= -1
        self.center = (self.center[0] + dx, self.center[1] + dy)
        self.canvas.move(self.handle, dx, dy)

    def displacement(self, c, d, cmax):
        '''
        Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.

        Arguments:
          c:    the center of the ball (x or y coordinate)
          cmax: the largest value in that direction
          d:    the desired displacement in that direction

        Return value: the computed displacement
        '''
        if c + d < self.radius:
            return d + (2 * (c - self.radius))
        if c + d > cmax - self.radius:
            return (2 * ((cmax - self.radius) - c)) - d
        return d

    def scale_speed(self, scale):
        '''
        Scale the speed of this object.

        Arguments:
          scale: the speed scaling factor

        Return value: none
        '''
        self.speed *= scale

    def delete(self):
        '''
        Remove this object from the canvas.

        Arguments: none
        Return value: none
        '''

        self.canvas.delete(self.handle)


def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''
    radius = random.randint(rmin, rmax)
    cx = random.randint(radius, xmax - radius)
    cy = random.randint(radius, ymax - radius)
    speed = random.randint(smin, smax)
    color = random_color()
    direction = random.randint(0, 360)
    return BouncingBall(canvas, (cx, cy), radius, color, direction, speed)

def random_color():
    '''Generates a random hex color.'''
    color = "#"
    c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += random.choice(c)
    return color

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q':
        done = True
    elif key == 'plus':  # add a ball at a random location
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))
    elif key == 'minus':  # remove a ball from the canvas if there are any
        if len(bouncing_balls) > 0:
            bouncing_balls[0].delete()
            bouncing_balls = bouncing_balls[1:]
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1.2)
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        for ball in bouncing_balls:
            ball.scale_speed(1 / 1.2)
    elif key == 'x':  # delete all bouncing_balls
        for ball in bouncing_balls:
            ball.delete()
        bouncing_balls = []

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)

    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        time.sleep(0.001)  # add a slight delay to smooth out the simulation
        for ball in bouncing_balls:
            ball.step()
        root.update()
