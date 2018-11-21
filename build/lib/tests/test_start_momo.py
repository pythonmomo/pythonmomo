import unittest
import pythonmomo.start_momo


class BasicTest(unittest.TestCase):
  def test_name_of_pythonmomo(self):
    self.assertEqual(pythonmomo.name, 'pythonmomo')
