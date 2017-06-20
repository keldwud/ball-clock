# name
# date
# description

# import modules
# need time for sleep
# need deque from collections to pop from bottom of stack
import time
from collections import deque

# accept input from user and validate input
def how_many_balls(balls):
  MIN_BALLS = 27
  MAX_BALLS = 127
  number_of_balls = balls
  while True:
    if number_of_balls >= MIN_BALLS and number_of_balls <= MAX_BALLS:
      print "Building clock with %s balls..." % (number_of_balls)
      return number_of_balls
    else:
      number_of_balls = input("How many balls in your clock (27 - 127)? ")

# create ball queue
queue_max = []
queue_max.extend(range(1,number_of_balls))
ball_queue = deque()

# operate ball queue
time.sleep(1)
print ball_queue
print ball_queue.popleft()
minute += 1
print minute

# minute balls

# five minute balls

# hour balls
