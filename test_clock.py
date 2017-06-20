import unittest
from clock import how_many_balls

class BallsTestCase(unittest.TestCase):
  """Tests for `ball-clock.py`."""

  def test_is_twenty_seven_valid(self):
    """Is twenty-seven successfully accepted?"""
    self.assertTrue(how_many_balls(27))

  def test_is_one_valid(self):
    """Is one correctly determined to be invalid input?"""
    self.assertTrue(how_many_balls(1))
    
if __name__ == '__main__':
  unittest.main()
