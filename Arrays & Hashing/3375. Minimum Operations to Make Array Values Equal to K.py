import unittest
from collections import defaultdict
from typing import List

class TestFindClosestNumber(unittest.TestCase):
    
    def test_minOperations(self):
        # Test case 1
        self.assertEqual(minOperations([5,2,5,4,5], 2), 2)
        
        # Test case 2
        self.assertEqual(minOperations([2,1,2], 2), -1)
        
        # Test case 3
        self.assertEqual(minOperations([9,7,5,3], 1), 4)
        

def minOperations(nums: List[int], k: int) -> int:
    count = 0
    hash_nums = defaultdict(int)
    for num in nums:
        if num < k: return -1
        if num not in hash_nums and num != k:
            hash_nums[num] += 1
            count += 1

    return count
    #Time Complexity = O(n) 
    #Space Complexity = O(n)

if __name__ == '__main__':
    unittest.main()
