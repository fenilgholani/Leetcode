/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> s=new ArrayList<>();
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        TreeNode root = null;
        
        if(root1 == null && root2 == null)
            return null;
            
        if(root1 != null && root2!= null)
            root = insert(root1, root2);
        else if(root1 == null && root2 != null)
            root = root2;
        else if(root1 != null && root2 == null)
            root = root1;
        
        inorder(root);
        Collections.sort(s);
        return s;
    }
    
    public TreeNode insert(TreeNode node, TreeNode root){
        
        if(root == null)
            return node;
        else if(root.val > node.val)
            root.left = insert(node, root.left);
        else
            root.right = insert(node, root.right);
        
        return root;
    }
    public void inorder(TreeNode t){
         if(t==null)
            return;

        inorder(t.left);
        s.add(t.val);
        inorder(t.right);   
    }
}