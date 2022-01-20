/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        
    
        ListNode curr = head;
        ListNode prev = head;
        while(curr != null){
            
            if(curr == head && curr.val == val){
                head = head.next;
            }
            
            else if(curr.val == val){
                
                if(curr.next != null && curr.next.val == val){
                    curr = curr.next;
                    continue;
                }
                
                prev.next = curr.next;
                
            }
            
            prev = curr;
            curr = curr.next;
            
            
        }
        return head;
    }
}