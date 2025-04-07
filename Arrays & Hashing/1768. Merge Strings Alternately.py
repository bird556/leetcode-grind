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
        word1 = "ab"
        word2 = "pqrs"
        expected1 = "apbqrs"
        self.assertEqual(mergeAlternately(word1, word2), expected1)
        
        # Test case 3
        word1 = "abcd"
        word2 = "pq"
        expected1 = "apbqcd"
        self.assertEqual(mergeAlternately(word1, word2), expected1)
        


def mergeAlternately(self, word1: str, word2: str) -> str:
    pass

if __name__ == '__main__':
    unittest.main()
