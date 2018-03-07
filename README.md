# Purpose

This is a repository where I put my stuff I try out with pygame under Python 3.6.
I am completely new to this, so my stuff is very basic.

### Things I learned about pygame

2018/03/07
The ball and paddles and everything are currently drawn as pygame.Rect(). What I did not know is that the position of a rectangle, i.e. if accessed via ball.x and ball.y are the topright corner of the rectangle. This gave me a headache because the ball was bouncing on thin air when I implemented the bounce with the left edge.


### test_ball_grav_move.py

Trying out two things:
1. Have a ball bounce under the influence of gravity. Collisions are fully elastic, no loss of energy
2. Move the ball by applying acceleration upon keypress of arrow keys, left and right.


