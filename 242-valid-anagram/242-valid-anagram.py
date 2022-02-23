class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for char in s:
            d1[char] = 1 + d1.get(char, 0)
        for char in t:
            d2[char] = 1 + d2.get(char, 0)
        return d1 == d2