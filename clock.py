#!/usr/bin/env python
"""This program should accept user input and return how many days until the clock repeats patterns"""

# import modules
# need time for sleep
# need deque from collections to pop from bottom of stack
import time
from collections import deque

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
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  SIXTY = 1
  queue_max = []
  queue_max.extend(range(1,how_many_balls()))
  print queue_max
  ball_queue = deque()
  time.sleep(SIXTY)
  print ball_queue
  print ball_queue.popleft()
  minute += 1
  print minute

# minute balls
def minute_balls(ball):
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  m = 0
  while m < 5:
    m += 1
  return ball;

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

  f = 0
  while f < 12:
    f += 1
  return ball;

# hour balls
def hour_balls(ball):
  """Asks user how many balls in the clock.

  Long description Ipsum Lorem
  
  Args:
    Ipsum Lorem

  Returns:
    Ipsum Lorem

  Raises:
    Ipsum Lorem

  """

  h = 0
  while h < 12:
    h += 1
  return ball;
  
run_ball_queue()
