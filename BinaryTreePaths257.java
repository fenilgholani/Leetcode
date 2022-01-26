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
    
    List <String> str = new ArrayList<>();
    
    public List<String> binaryTreePaths(TreeNode root) {
     
        String s="";
        path(root, s);
        // System.out.println(str);
        return str;
    }
    
    public void path(TreeNode root, String s){
        
        if(root == null)           
            return;

        s+=root.val+"->";
        // System.out.println(s);
        path(root.left,s);
        path(root.right,s);
        
        if(root.left == null && root.right == null)
            str.add(s.substring(0,s.length()-2));    
    }
    
}