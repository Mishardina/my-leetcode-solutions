#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for outer_num in nums:
            if outer_num-1 not in nums:
                inner_num = outer_num + 1
                while inner_num in nums:
                    inner_num += 1
                longest = max(longest, inner_num - outer_num)
        return longest