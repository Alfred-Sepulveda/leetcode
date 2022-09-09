#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2:ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1.val and list2.val:
            if list1 < list2:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

#mistakes were not remembering tail = dummy, tail = tail.next and tail.next = list1
# also while loop contained list1.val 


