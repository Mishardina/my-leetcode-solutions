# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        list_len = 0
        while curr_node:
            list_len += 1
            curr_node = curr_node.next
        
        middle_node = list_len // 2
        
        if middle_node == 0:
            head = None
            return head
        
        curr_node = head
        for i in range(middle_node-1):
            curr_node = curr_node.next
        
        curr_node.next = curr_node.next.next
        
        return head