import unittest
from typing import List

class TestFindClosestNumber(unittest.TestCase):
    
    def test_find_closest_number(self):
        # Test case 1
        nums1 = [-4, -2, 1, 4, 8]
        expected1 = 1
        self.assertEqual(findClosestNumber(nums1), expected1)
        
        # Test case 2
        nums2 = [2, -1, 1]
        expected2 = 1
        self.assertEqual(findClosestNumber(nums2), expected2)
        
        # You can add more test cases here as needed


def findClosestNumber(nums: List[int]) -> int:
    pass

if __name__ == '__main__':
    unittest.main()
