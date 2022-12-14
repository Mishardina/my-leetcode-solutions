#https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2
            mid_val = nums[mid]

            if mid_val < target:
                start = mid + 1
            elif mid_val > target:
                end = mid - 1
            else:
                return mid

        return start