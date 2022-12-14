#https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen = [0] * 52

        for l, r in ranges:
            seen[l] += 1
            seen[r + 1] -= 1

        for i in range(1, 52):
            seen[i] += seen[i - 1]

        return all(seen[i] for i in range(left, right + 1))