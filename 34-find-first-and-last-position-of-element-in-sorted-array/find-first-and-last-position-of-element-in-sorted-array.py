class Solution(object):
    def searchRange(self, nums, target):

        def lowerBound():
            l, h = 0, len(nums) - 1
            ans = len(nums)
            while l <= h:
                m = (l + h) // 2
                if nums[m] >= target:
                    ans = m
                    h = m - 1
                else:
                    l = m + 1
            return ans

        def upperBound():
            l, h = 0, len(nums) - 1
            ans = len(nums)
            while l <= h:
                m = (l + h) // 2
                if nums[m] > target:
                    ans = m
                    h = m - 1
                else:
                    l = m + 1
            return ans

        first = lowerBound()
        last = upperBound() - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, last]