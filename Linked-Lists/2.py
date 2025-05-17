'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node for storing the list of added values
        dummy_head = ListNode(0)
        # Curr variable acts as a pass by reference
        curr = dummy_head
        # Will change if we get a sum of 10 or more
        carry = 0
        # Will add nodes as long as we have a carry or are still traversing the nodes
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Perform the correct addition
            sum_val = val1 + val2 + carry
            # We have a carry if sum_val is 10 or more
            carry = sum_val // 10
            # Initialize the next node
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
            # Traverse to the next node only where necessary
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next