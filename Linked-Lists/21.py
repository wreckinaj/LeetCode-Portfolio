'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy variable
        head = ListNode()
        # Will update the list with head as we go along
        cur = head
        # Check values one at a time since lists are sorted
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        # Append what is left after we traverse through one list
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return head.next