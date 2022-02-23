class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = ans = 0
        for right, val in enumerate(s):
            while val in chars:
                chars.remove(s[left])
                left += 1
            chars.add(val)
            ans = max(ans, right - left + 1)
        return ans