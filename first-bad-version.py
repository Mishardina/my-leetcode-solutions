#https://leetcode.com/problems/first-bad-version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2
            mid_val = nums[mid]

            #if mid_val < target:
            if not isBadVersion(mid):
                start = mid + 1
            elif mid_val > target:
                end = mid - 1
            else:
                return mid

        return start