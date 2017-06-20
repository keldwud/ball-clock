import unittest
from clock import how_many_balls
from clock import minute_balls
from clock import five_minute_balls
from clock import hour_balls


class BallsTestCase(unittest.TestCase):
  """Tests for `ball-clock.py`."""

  def test_is_twenty_seven_valid(self):
    """Is twenty-seven successfully accepted?"""
    self.assertTrue(how_many_balls(27))

  def test_is_one_valid(self):
    """Is one-hundred-twenty-seven correctly determined to be invalid input?"""
    self.assertTrue(how_many_balls(127))

  def test_minute_balls(self):
    """Testing minute balls"""
    self.assertTrue(minute_balls())
  
  def test_five_minute_balls(self):
    """Testing five minute balls"""
    self.assertTrue(five_minute_balls())
  
  def test_hour_balls(self):
    """Testing hour balls"""
    self.assertTrue(hour_balls())

if __name__ == '__main__':
  unittest.main()
