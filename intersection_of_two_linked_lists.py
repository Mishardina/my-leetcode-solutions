# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        intersection = None
        currentA = headA
        currentB = headB
        
        lenA = 1
        lenB = 1
        
        while currentA:
            lenA += 1
            currentA = currentA.next
            
        while currentB:
            lenB += 1
            currentB = currentB.next
        
        currentA = headA
        currentB = headB
        
        if lenA > lenB:
            while lenA != lenB:
                currentA = currentA.next
                lenA -= 1
        elif lenA < lenB:
            while lenA != lenB:
                currentB = currentB.next
                lenB -= 1
                
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        
        return intersection