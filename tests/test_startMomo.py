import unittest
import pythonmomo.startmomo

class BasicTest(unittest.TestCase):
  def test_name_of_pythonmomo(self):
    self.assertEqual(pythonmomo.name, 'pythonmomo')
