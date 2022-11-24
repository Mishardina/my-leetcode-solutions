#https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:      
        start = 0
        end = len(arr) - 1   
        while start <= end:
            mid = (start + end) // 2
            lesser_nums = arr[mid] - (mid + 1)

            if lesser_nums == k:
                if mid > 0 and (arr[mid - 1] - mid) == k:
                    end = mid - 1
                    continue
        
                return arr[mid] - 1

            if lesser_nums < k:
                start = mid + 1
            elif k < lesser_nums:
                end = mid - 1

        if end < 0:
            return k

        less = arr[end] - (end + 1)
        k -= less

        return arr[end] + k