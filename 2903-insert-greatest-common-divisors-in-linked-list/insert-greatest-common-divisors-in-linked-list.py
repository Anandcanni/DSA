# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        c = head.next
        while c:
            gcd = math.gcd(c.val ,p.val)
            g = ListNode(gcd)
            p.next =g
            g.next =c
            p =c
            c = c.next
        return head
        

        