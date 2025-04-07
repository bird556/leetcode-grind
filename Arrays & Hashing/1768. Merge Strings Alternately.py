import unittest
from typing import List

class TestMergeStringAlt(unittest.TestCase):
    
    def test_merge_string_alt(self):
        # Test case 1
        word1 = "abc"
        word2 = "pqr"
        expected1 = "apbqcr"
        self.assertEqual(mergeAlternately(word1, word2), expected1)
        
        # Test case 2
        self.assertEqual(mergeAlternately("ab", "pqrs"), "apbqrs")
        
        # Test case 3
        self.assertEqual(mergeAlternately("abcd", "pq"), "apbqcd")
        


def mergeAlternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    m, n = len(word1), len(word2)
    merge_s = ''
    while i < m or j < n:
        if i < m:
            merge_s += word1[i]
            i += 1
        if j < n:
            merge_s += word2[j]
            j += 1
    return merge_s

if __name__ == '__main__':
    unittest.main()
