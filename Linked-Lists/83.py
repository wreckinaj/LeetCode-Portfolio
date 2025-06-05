'''
Given the head of a sorted linked list, delete all duplicates such that each element
appears only once. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Store result in a dummy variable
        res = head
        while head and head.next:
            # We make the next node the next new number with this statement
            if head.val == head.next.val:
                head.next = head.next.next
            # We move to the next one when we find no more duplicates of the current number
            else:
                head = head.next
        return res