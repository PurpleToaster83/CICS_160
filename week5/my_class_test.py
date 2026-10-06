import unittest
from my_class import Counter

class Test_Counter(unittest.TestCase):
    def setUp(self):
        self.obj = Counter(10)

    def tearDown(self):
        del self.obj

    def test_add_one(self):
        val = self.obj.inc()
        msg = ''
        if val>11:
            msg=f'Looks like you increased too much, returned value was {val}'
        elif val<11:
            msg=f'Looks like you decreased, returned value was {val}'
        self.assertEqual(val, 11, msg=msg)
        self.assertEqual(self.obj.value, 11, msg="returned correct value, but did not save")

    def test_value_type(self):
        self.assertIsInstance(self.obj.value, int)

if __name__ == '__main__':
    unittest.main() # looks for class that inherits from TestCase and runs every test