class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = []
        if len(s) != len(t):
            return False
        for char in s:
            d.append(char)
        for char in t:
            if char in d:
                d.remove(char)
        return len(d) == 0