#!/usr/bin/env python

import unittest
from clock import how_many_balls
from clock import minute_balls
from clock import five_minute_balls
from clock import hour_balls
from clock import run_ball_queue

class BallsTestCase(unittest.TestCase):
  """Tests for `ball-clock.py`."""

  def test_how_many_balls_min_balls(self):
    """Is twenty-seven successfully accepted?"""
    self.assertTrue(how_many_balls(27))

  def test_how_many_balls_max_balls(self):
    """Is one-hundred-twenty-seven correctly determined to be invalid input?"""
    self.assertTrue(how_many_balls(127))

  def test_ball_queue(self):
    """Testing ball queue"""
    self.assertTrue(run_ball_queue())

  def test_minute_balls(self):
    """Testing minute balls"""
    self.assertTrue(minute_balls())
  
  # add test for 5
  
  def test_five_minute_balls(self):
    """Testing five minute balls"""
    self.assertTrue(five_minute_balls())
  
  # add test for 12
  
  def test_hour_balls(self):
    """Testing hour balls"""
    self.assertTrue(hour_balls())

  # add test for 1 and 12

if __name__ == '__main__':
  unittest.main()
