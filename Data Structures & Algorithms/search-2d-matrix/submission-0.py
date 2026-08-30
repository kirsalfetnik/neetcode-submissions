class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_list = []

        for i in matrix:
            total_list += i
        
        l, r = 0, len(total_list)-1

        while (l <= r):
            mid = (l + r) // 2

            if target == total_list[mid]:
                return True
            elif target > total_list[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False 