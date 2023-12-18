# imports from the standard Python library so no "from" is required
import unittest

# function to test
def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

# containers for tests
row_nums = [x for x in range(1, 41)]
test_nums = [x for x in range(1, 44, 2)]

# boolean testers
x = 1 < 2
y = 1 > 2
z = 'a string'

# ******* IMPORTANT!!! ALL TEST FUNCTIONS MUST BEGIN WITH THE WORD "test" *******
# grouping the tests for this function into a class that inherits from unittest.TestCase
class NearestExitTests(unittest.TestCase):

# defining test functions
  def test_row_1(self):
    # self.assertEqual takes 3 arguments --- 1. the function call with args to test, 2. the expected output, 3. what to say if it fails
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

# assertEqual() is not the only test.
# Let's try a new one here... assertIn(value, container)
  def test_row_1_in_row_nums(self):
    self.assertIn(1, row_nums)
    
  def test_row_20_in_row_nums(self):
    self.assertIn(20, row_nums)
    
  def test_row_40_in_row_nums(self):
    self.assertIn(40, row_nums)
    
  # def test_row_41_in_row_nums(self): <---- This fails, as expected.
  #   self.assertIn(41, row_nums)

# We also have assertTrue(value)... check it out
  def test_x(self):
    self.assertTrue(x)
    
  # def test_y(self):         <---- This fails, as expected.
  #   self.assertTrue(y)

# We can skip tests based on conditions like so
  # @unittest.skipIf(type(z) is str, 'this test is for booleans, not strings')
  # or
  # @unittest.skipUnless(type(z) is not str, 'this does not test strings')
  # or (inside function call)
  def test_z(self):
    if type(z) is not bool:
      self.skipTest('This only tests boolean values')
    self.assertTrue(z)
  
# This is kind of a greatest hits version of assert methods in unittest but there are a crapload of deep tracks.
# You can basically assert anything you can think of and then test it in this way. Very cool.
# Other assertions worth noting: assertLess, assertAlmostEqual, assertRaises,   

# We can also test lots of values at once with the self.subTest() function
  def test_lots_of_row_nums(self):
    for test_num in test_nums:
      with self.subTest(test_num):
        self.assertIn(test_num, row_nums)   
# The above function tests every item in test_nums against row_nums, and because we've provided self.subTest a value of "test_num", each failure will be logged out to our terminal so we can see exactly which elements are failing the test 




# run tests
unittest.main()