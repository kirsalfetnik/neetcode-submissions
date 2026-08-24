class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = 201

        for i in strs:
            if len(i) < shortest:
                shortest = len(i)

        prefix = ""
        my_set = set()
        counter = 0

        while counter < (shortest):

            for i in strs:
                my_set.add(i[counter])

            if len(my_set) != 1:
                return prefix
            else:
                prefix += my_set.pop()
                my_set.clear()

            counter += 1
        
        return prefix
