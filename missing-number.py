#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = 0
        ref_sum = 0
        for i in range(len(nums)):
            ref_sum += i+1
            nums_sum += nums[i]
        
        return ref_sum - nums_sum