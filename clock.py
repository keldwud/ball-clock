#!/usr/bin/env python
"""This program should accept user input and return how many days until the clock repeats patterns"""

# import modules
# need time for sleep
# need deque from collections to pop from bottom of stack
import time
from collections import deque

# create variables
ball_queue = []
minute_queue = []
five_queue = []
hour_queue = []

queue_max = []


# accept input from user and validate input
def how_many_balls():
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """
  MIN_BALLS = 27
  MAX_BALLS = 127
  # number_of_balls = balls
  number_of_balls = 0
  while True:
    if number_of_balls >= MIN_BALLS and number_of_balls <= MAX_BALLS:
      print "Building clock with %s balls..." % (number_of_balls)
      return number_of_balls
    else:
      number_of_balls = input("How many balls in your clock (27 - 127)? ")

# create ball queue
# operate ball queue
def run_ball_queue():
  """Fills the ball queue and transfers a ball into minute queue every 60 seconds.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  SIXTY = 1
  queue_max.extend(range(1,how_many_balls()))
  print queue_max
  ball_queue = deque(queue_max)
  time.sleep(SIXTY)
  print ball_queue
  ball = ball_queue.popleft()
  print ball
  ball_queue.append(minute_balls(ball))

# minute balls
def minute_balls(ball):
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Every minute, the least recently used ball is removed from the queue of balls at the bottom of the clock, elevated, then deposited on the minute indicator track, which is able to hold four balls. When a fifth ball rolls on to the minute indicator track, its weight causes the track to tilt.

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  while len(minute_queue) < 5:
    minute_queue.append(ball)
  while len(minute_queue) > 0:
    return minute_queue.popleft()
  five_minute_balls(ball)
    
# five minute balls
def five_minute_balls(ball):
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  while len(five_queue) < 12:
    five_queue.append(ball)
  while len(five_queue) > 0:
    return five_queue.popleft()
  hour_balls(ball)
    
# hour balls
def hour_balls():
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """
  while len(hour_queue) < 12:
    hour_queue.append(ball)
  while len(hour_queue) > 0:
    return hour_queue.popleft()

run_ball_queue()
