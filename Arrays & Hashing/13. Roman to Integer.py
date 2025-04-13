import unittest
from collections import defaultdict
from typing import List

class TestRomanToIntegers(unittest.TestCase):
    
    def test_minOperations(self):
        # Test case 1
        self.assertEqual(romanToInt("III"), 3)
        
        # Test case 2
        self.assertEqual(romanToInt("LVIII"), 58)

        
        # Test case 3
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

        

def romanToInt(s: str) -> int:
    count = 0
    hash_roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    n, m = 0, len(s)

    while n < m:
        num = hash_roman[s[n]]
        if (n + 1) < m and num < hash_roman[s[n + 1]]:
            count += hash_roman[s[n + 1]] - num
            n += 2
        else:
            count += num
            n += 1

    return count
    #Time Complexity = O(n) 
    #Space Complexity = O(n)

if __name__ == '__main__':
    unittest.main()
