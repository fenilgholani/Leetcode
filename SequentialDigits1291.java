class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        
        int num = 0;
        
        List <Integer>ans = new ArrayList<>();
        
        for(int i = 1; i<10 ; i++)
        {
            num = i;
            for(int j = i+1;j<10;j++)
            {
                num = num*10 + j;
                if(num >= low && num <= high)
                {
                    ans.add(num);
                }
            }
        }
        Collections.sort(ans);
        // System.out.println(ans);
        
        return ans;
    }
}