class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f, s = 0, len(matrix) - 1
        required_list = None

        while (f <= s):
            mid = (f + s) // 2
            if (matrix[mid][0] == target or matrix[mid][-1] == target):
                return True
            elif (matrix[mid][0] > target):
                s = mid - 1
            elif (matrix[mid][0] < target and matrix[mid][-1] < target):
                f = mid + 1
            elif (matrix[mid][0] < target and matrix[mid][-1] > target):
                required_list = matrix[mid]
                break
        
        if required_list == None:
            return False
        else:
            l, r = 0, len(required_list) - 1
             
            while (l <= r):
                mid = (l + r) // 2

                if target == required_list[mid]:
                    return True
                elif target > required_list[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            return False
            
        