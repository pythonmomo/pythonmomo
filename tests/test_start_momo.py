import unittest
from pythonmomo.start_momo import return_name


class BasicTest(unittest.TestCase):
  def test_name_of_pythonmomo(self):
    self.assertEqual(return_name(), 'pythonmomo')
