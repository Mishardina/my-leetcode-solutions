#https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def mergeSort(heights, names):
            if len(heights)>1:
                mid = len(heights)//2
                left_half_heights = heights[:mid]
                right_half_heights = heights[mid:]

                left_half_names = names[:mid]
                right_half_names = names[mid:]

                mergeSort(left_half_heights, left_half_names)
                mergeSort(right_half_heights, right_half_names)

                i = 0
                j = 0
                k = 0
                while i < len(left_half_heights) and j < len(right_half_heights):
                    if left_half_heights[i] > right_half_heights[j]:
                        heights[k] = left_half_heights[i]
                        names[k] = left_half_names[i]
                        i=i+1
                    else:
                        heights[k] = right_half_heights[j]
                        names[k] = right_half_names[j]
                        j=j+1
                    k=k+1

                while i < len(left_half_heights):
                    heights[k] = left_half_heights[i]
                    names[k] = left_half_names[i]
                    i = i + 1
                    k = k + 1

                while j < len(right_half_heights):
                    heights[k] = right_half_heights[j]
                    names[k] = right_half_names[j]
                    j = j + 1
                    k = k + 1
        
        mergeSort(heights, names)

        return names