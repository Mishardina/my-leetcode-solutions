#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in nums:
                current = i
                streak = 0
                while i in nums:
                    i+=1
                    streak+=1
                    longest = max(longest,streak)
        return longest