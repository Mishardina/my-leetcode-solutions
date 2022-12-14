#https://leetcode.com/problems/squares-of-a-sorted-array

def square(num):
    return num**2

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i=i+1
            else:
                arr[k] = right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            arr[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j = j + 1
            k = k + 1

class Solution:  
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(square, nums))
        mergeSort(nums)

        return nums