# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        start = head
        end = head
        summ = 0

        newhead = ListNode(0)
        curr = newhead

        while start.next != None:
            
            summ += end.val
            end = end.next

            if end.val == 0:
                newnode = ListNode(summ)
                curr.next = newnode
                curr = curr.next
                summ = 0
                start = end
        
        return newhead.next