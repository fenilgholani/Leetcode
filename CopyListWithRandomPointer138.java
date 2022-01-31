/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        HashMap <Node, Node> h= new HashMap<>();
        
        Node curr = head;
        
        while(curr != null){
            h.put(curr,new Node(curr.val));
            curr = curr.next;
        }
        
        curr = head;
        Node head2=null;
        Node curr2= null;
        while(curr != null){
            
           curr2 = h.get(curr);
            curr2.next = h.get(curr.next);
            curr2.random = h.get(curr.random);
            
            if(head2 == null)
                head2 = curr2;
            
            curr = curr.next;
            curr2 = curr2.next;
        }
        
        return head2;
        
    }
}