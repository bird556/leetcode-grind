import unittest
from collections import defaultdict
from typing import List

class TestFindClosestNumber(unittest.TestCase):
    
    def test_topKFrequent(self):
        # Test case 1
        self.assertEqual(topKFrequent([1,1,1,2,2,3], 2), [1,2])
        
        # Test case 2
        self.assertEqual(topKFrequent([1], 1), [1])
        

def topKFrequent(nums: List[int], k: int) -> int:
    top_k = []
    hash_nums = defaultdict(int)
    for num in nums:
        hash_nums[num] += 1
    top_k = [key for key, val in sorted(hash_nums.items(), key=lambda x: x[1], reverse=True)[:k]]
    return top_k
    #Time Complexity = O(n logn) 
    #Space Complexity = O(n)

if __name__ == '__main__':
    unittest.main()
