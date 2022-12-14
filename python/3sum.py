#https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for j in range(i+1, len(nums)):
                if -nums[i] - nums[j] in seen:
                    out.append([nums[i], nums[j], -nums[i]-nums[j]])
                    while j + 1 < len(nums) and nums[j+1] == nums[j]:
                        j += 1
                seen.add(nums[j])
        out = list(map(list,set(map(tuple, out))))
        return out