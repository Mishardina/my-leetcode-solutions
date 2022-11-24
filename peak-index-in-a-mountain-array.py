#https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2 
            if arr[mid - 1] > arr[mid]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                start = mid
            else:
                return mid