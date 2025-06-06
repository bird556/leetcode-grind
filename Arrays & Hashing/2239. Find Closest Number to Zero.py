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
        

def findClosestNumber(nums: List[int]) -> int:
    closetNum = abs(nums[0])
    for i in range(1, len(nums)):
        if abs(nums[i]) < abs(closetNum):
            closetNum = nums[i]
    
    return abs(closetNum) if closetNum < 0 and abs(closetNum) in nums else closetNum
    #Time Complexity = O(n) 
    #Space Complexity = O(1)

if __name__ == '__main__':
    unittest.main()
