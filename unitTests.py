import unittest
from arraylist import *

class ArrayListTest(unittest.TestCase):

    def test_add(self):
        arrayList = ArrayList()
        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)
        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)
        self.assertEqual("[5, 5, 2, 3, 5, 5, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None]", arrayList.print())
    
    def test_insert(self):
        arrayList = ArrayList()
        arrayList.insert(0, 5)
        arrayList.insert(0, 7)
        arrayList.insert(1, 8)
        arrayList.insert(-5, 12)
        arrayList.insert(10, 15)
        arrayList.insert(2, 3)
        self.assertEqual("[7, 8, 3, 5, None, None, None, None, None, None]", arrayList.print())

    def test_get(self):
        arrayList = ArrayList()
        self.assertEqual(-1, arrayList.get(0))
        self.assertEqual(-1, arrayList.get(-3))

        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)

        self.assertEqual(-1, arrayList.get(4))
        self.assertEqual(5, arrayList.get(1))

    def test_remove(self):
        arrayList = ArrayList()
        self.assertEqual(-1, arrayList.remove(0))

        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)
        self.assertEqual(-1, arrayList.remove(4))
        arrayList.remove(1)
        self.assertEqual("[5, 2, 3, None, None, None, None, None, None, None]", arrayList.print())

    def test_size(self):
        arrayList = ArrayList()
        self.assertEqual(0, arrayList.size())

        arrayList.add(5)
        arrayList.add(5)
        arrayList.insert(1, 3)
        arrayList.remove(0)
        self.assertEqual(2, arrayList.size())

    def test_is_empty(self):
        arrayList = ArrayList()
        self.assertEqual(True, arrayList.is_empty())

        arrayList.add(5)
        arrayList.add(5)
        self.assertEqual(False, arrayList.is_empty())
        arrayList.remove(0)
        arrayList.remove(0)
        self.assertEqual(True, arrayList.is_empty())
    
    def test_resize(self):
        arrayList = ArrayList()
        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)
        arrayList.add(5)
        arrayList.add(5)
        arrayList.add(2)
        arrayList.add(3)
        self.assertEqual(10, arrayList.size())

if __name__ == '__main__':
    unittest.main()



