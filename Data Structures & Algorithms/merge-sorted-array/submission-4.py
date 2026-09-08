class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f = m - 1
        s = n - 1
        end = len(nums1) - 1

        while f >= 0 and s >= 0 and f >= 0:
            if nums1[f] > nums2[s]:
                nums1[end] = nums1[f]
                end -= 1
                f -= 1
            else: 
                nums1[end] = nums2[s]
                end -= 1
                s -= 1
        
        while end >= 0 and s >= 0:
            nums1[end] = nums2[s]
            end -= 1
            s -= 1

        

        