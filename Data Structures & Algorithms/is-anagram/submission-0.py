class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        
        for i in s:
            if i in dict_s.keys():
                dict_s[i] += 1
            elif i not in dict_s.keys():
                dict_s[i] = 0

        for i in t:
            if i in dict_t.keys():
                dict_t[i] += 1
            elif i not in dict_t.keys():
                dict_t[i] = 0

        return dict_t == dict_s