class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for i in range(0, len(strs)):
            temp = [0] * 26
            for j in strs[i]:
                temp[ord(j) - ord('a')] += 1
            res[tuple(temp)].append(strs[i])

        return list(res.values())
