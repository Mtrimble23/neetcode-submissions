from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1
        
        for char in t:
            if char in counts:
                counts[char] -= 1

        for val in counts.values():
            if val != 0:
                return False
        return True