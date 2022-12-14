#https://leetcode.com/problems/subarray-sum-equals-k

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_dict = defaultdict(lambda : 0)
        print(nums_dict.items())
        count = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == k:
                count += 1
            if (curr_sum - k) in nums_dict:
                count += nums_dict[curr_sum - k]
            nums_dict[curr_sum] += 1

        return count