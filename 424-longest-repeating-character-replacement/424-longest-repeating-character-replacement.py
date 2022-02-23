class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        maxFreq = ans = left = 0
        for right, val in enumerate(s):
            d[val] = 1 + d.get(val, 0)
            maxFreq = max(maxFreq, d[val])
            if (right - left + 1) - maxFreq > k:
                d[s[left]] -= 1
                left += 1
        return (right - left + 1)