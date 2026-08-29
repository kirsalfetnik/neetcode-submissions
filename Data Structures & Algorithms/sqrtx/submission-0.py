class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        if x == 1 or x == 0:
            return x

        while l <= r:
            mid = (l + r + 1) // 2
            if (mid * mid) == x:
                return mid
            elif ((mid * mid) < x) and (((mid+1) * (mid+1)) > x):
                return mid
            elif ((mid * mid) < x) and (((mid+1) * (mid+1)) < x):
                l = mid + 1
            elif ((mid * mid) > x) and (((mid+1) * (mid+1)) > x):
                r = mid - 1
            elif ((mid * mid) < x) and (((mid+1) * (mid+1)) == x):
                return mid + 1
            else:
                return 666

        return 777
