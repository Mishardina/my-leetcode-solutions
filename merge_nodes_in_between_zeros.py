# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_zero_node = head
        curr_node = head.next
        curr_sum = 0
        while curr_node:
            if curr_node.val != 0:
                curr_sum += curr_node.val
                curr_node.val = 0
            else:
                curr_node.val = curr_sum
                curr_sum = 0
                prev_zero_node.next = curr_node
                prev_zero_node = curr_node
            curr_node = curr_node.next
        return head.next