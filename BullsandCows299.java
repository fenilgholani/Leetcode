class Solution {
    public String getHint(String secret, String guess) {
 
        int bull = 0, cow = 0;
        int s[]= new int[10];
        int g[] = new int[10];
        char secret1[] = secret.toCharArray();
        char guess1[] = guess.toCharArray();
        
        for(int i=0;i<secret1.length;i++){
            
            if(secret1[i] == guess1[i])
                bull++;
            
            else{
                s[secret1[i]-'0']++;
                g[guess1[i]-'0']++;
                
            }
        }   
        
        for(int i=0;i<s.length;i++){
            cow += (int)Math.min(s[i],g[i]);
        }
        
        // System.out.println(bull);
        // System.out.println(cow);
        return ""+bull+"A"+cow+"B";
    }
    
    
}