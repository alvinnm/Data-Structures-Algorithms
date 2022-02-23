class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for char in strs:
            ans[''.join(sorted(char))].append(char)
        return ans.values()