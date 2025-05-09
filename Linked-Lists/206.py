'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use this to store the previous node obtained
        prev = None
        # Use to keep track of each node progressed
        curr = head
        while curr:
            # Use a temp variable to avoid overwriting
            temp = curr.next
            # Perform the swap
            curr.next = prev
            prev = curr
            curr = temp
        return prev