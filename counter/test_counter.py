"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest
class CounterTest(unittest.TestCase):

    def setUp(self):
        self.a = Counter()

    def test_is_singleton(self):
        self.b = Counter()
        self.a.increment()
        self.assertEquals(self.a, self.b)


    def test_is_reset(self):
        self.a.increment()
        self.b = Counter()
        self.assertEquals(self.a,self.b)



    def test_is_same_instance(self):
        self.b = Counter()
        self.assertIsInstance(self.a , Counter)
        self.assertIsInstance(self.b, Counter)
        self.assertEquals(self.a, self.b)














