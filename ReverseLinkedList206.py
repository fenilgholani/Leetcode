# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        elif head.next == None:
            return head
        
        # self.reverseList(head.next)
        # newnode = ListNode(head.val)
        # head.next = newnode

        # return head
        curr = head
        prev = None
        while curr != None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
            
            # print(n)

        return prev



