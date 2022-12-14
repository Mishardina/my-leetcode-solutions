#https://leetcode.com/problems/sort-an-array
#Contains both merge- and count- sort

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

def countsort(arr):
    n = len(arr)
    k = max(arr)
    arr_min = min(arr)
    freq = [0 for i in range(arr_min, k+1)]
    res = [0] * n

    for i in range(n):
        freq[arr[i] - arr_min] += 1

    for j in range(1, len(freq)):
        freq[j] += freq[j-1]

    for i in range(n-1, -1, -1):
        res[freq[arr[i] - arr_min] - 1] = arr[i]
        freq[arr[i] - arr_min] -= 1

    return res

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #mergeSort(nums)
        nums = countsort(nums)
        return nums