import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
    
    def test_all(self):
        o = OrderedList()
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        
        # Basic Test
        self.assertFalse(o.is_empty())
        self.assertEqual(o.size(), 5)
        self.assertEqual(o.python_list(), [1,2,3,4,5])
        self.assertEqual(o.python_list_reversed(), [5,4,3,2,1])
        self.assertFalse(o.add(1), False)
        self.assertEqual(o.pop(4), 5)
        o.add(5)
        
        # Testing if items are at correct index
        self.assertEqual(o.index(1), 0)
        self.assertEqual(o.index(2), 1)
        self.assertEqual(o.index(3), 2)
        self.assertEqual(o.index(4), 3)
        self.assertEqual(o.index(5), 4)
        self.assertEqual(o.index(6), None)

        # Testing if search method works
        self.assertTrue(o.search(1))
        self.assertTrue(o.search(2))
        self.assertTrue(o.search(3))
        self.assertTrue(o.search(4))
        self.assertTrue(o.search(5))

        # Testing if return false if not in list for search method
        self.assertFalse(o.search(6))
        self.assertFalse(o.search(7))
        self.assertFalse(o.search(0))
        self.assertFalse(o.search(-1))

        # Testing pop and size   
        self.assertEqual(o.pop(0), 1)
        self.assertEqual(o.size(), 4)

        with self.assertRaises(IndexError):
            o.pop(9)
        
        self.assertEqual(o.pop(0), 2)
        self.assertEqual(o.size(), 3)
        
        self.assertEqual(o.pop(0), 3)
        self.assertEqual(o.size(), 2)
        
        self.assertEqual(o.pop(0), 4)
        self.assertEqual(o.size(), 1)
        
        self.assertEqual(o.pop(0), 5)
        self.assertEqual(o.size(), 0)

        # Testing case if its empty
        self.assertEqual(o.python_list(), [])
        self.assertEqual(o.python_list_reversed(), [])

        # Testing if empty
        self.assertTrue(o.is_empty())

        with self.assertRaises(IndexError):
            o.pop(1)
        
        with self.assertRaises(IndexError):
            o.pop(0)
        
        with self.assertRaises(IndexError):
            o.search(3)
        
        with self.assertRaises(IndexError):
            o.index(1)
        
        with self.assertRaises(IndexError):
            o.remove(1)
        
        # Testing remove
        o.add(1)
        self.assertEqual(o.remove(2), False)
        self.assertEqual(o.remove(1), True)

        o.add(1)
        o.add(2)
        self.assertEqual(o.remove(2), True)
        o.remove(1)

        o.add(1)
        o.add(2)
        o.add(3)
        self.assertEqual(o.remove(2), True)
        self.assertEqual(o.remove(4), False)
        o.remove(1)
        o.remove(3)

        
        # Testing add method
        self.assertTrue(o.add(1))
        self.assertTrue(o.add(2))
        self.assertTrue(o.add(3))
        self.assertTrue(o.add(5))
        self.assertTrue(o.add(4))

        self.assertFalse(o.add(1))
        self.assertFalse(o.add(2))
        self.assertFalse(o.add(3))
        self.assertFalse(o.add(5))

    def test_node(self):
        o = OrderedList()
        
        with self.assertRaises(ValueError):
            print(Node(1) < 1)
        
        self.assertTrue(Node(1) < Node(2))
        o.add(10)
        o.add(20)
        self.assertTrue(o.add(5))
        self.assertTrue(o.add(15))

        

if __name__ == '__main__': 
    unittest.main()
