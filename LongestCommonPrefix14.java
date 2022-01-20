class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int min = strs[0].length(), pos = 0;
        

        for(int i = 0; i <strs.length; i++){

            if(min > strs[i].length()){
                min = strs[i].length();
                pos = i;
            }
        }
        int i=0;
        // System.out.println(strs[pos]);
        for(int j = strs[pos].length()-1; j>=0; j--){
            for(i=0;i<strs.length;i++){
                if(!strs[i].startsWith(strs[pos].substring(0,j+1)))
                    break;    
                
            }
            if(i == strs.length)
                if(j == 0)
                    return strs[pos].substring(0,1);
                else
                    return strs[pos].substring(0,(j+1));
        }
        
        return "";
    }
}