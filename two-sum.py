#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_positions = {}
        for i in range(0, len(nums)):
            if target-nums[i] in nums_positions:
                return [nums_positions[target-nums[i]], i]
            nums_positions[nums[i]] = i