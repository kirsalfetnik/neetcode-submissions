class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        F, S = m-1, n-1
        T = len(nums1)-1

        while F >= 0 and S >= 0:
            if nums1[F] >= nums2[S]:
                nums1[T] = nums1[F]
                T -= 1
                F -= 1
            else:
                nums1[T] = nums2[S]
                T -= 1
                S -= 1
        
        while S >= 0:
            nums1[T] = nums2[S]
            T -= 1
            S -= 1

        