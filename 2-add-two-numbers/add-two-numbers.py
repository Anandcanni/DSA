# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Anand
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_values = []
        l2_values = []
        curr= l1
        while curr:
            l1_values.append(str(curr.val))
            curr = curr.next

        curr =l2
        while curr:
            l2_values.append(str(curr.val))
            curr = curr.next
        l1_values = l1_values[::-1]
        l2_values = l2_values[::-1]

        l1_nums = int(''.join(l1_values))
        l2_nums = int(''.join(l2_values))

        new_digit = str(l1_nums + l2_nums)[::-1]
        dummy = ListNode()
        curr =dummy
        for d in new_digit:
            curr.next = ListNode(int(d))
            curr =curr.next
        return dummy.next
