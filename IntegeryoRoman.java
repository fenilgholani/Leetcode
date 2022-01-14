class Solution {
    public String intToRoman(int num) {
        
        int num1 = num, n = 0, r = 0, count = 0; 
        String s ="";
        while(num1 != 0){
            count++;
            r = num1 % 10;
            num1 /= 10;
            
            if(count == 1){
                switch(r){
                    case 1:
                        s = "I" + s;
                        break;
                    case 2:
                        s = "II" + s;
                        break;
                    case 3:
                        s = "III" + s;
                        break;
                    case 4:
                        s = "IV" + s;
                        break;
                    case 5:
                        s = "V" + s;
                        break;
                    case 6:
                        s = "VI" + s;
                        break;
                    case 7:
                        s = "VII" + s;
                        break;
                    case 8:
                        s = "VIII" + s;
                        break;
                    case 9:
                        s = "IX" + s;
                        break;
                    default:
                        break;
                }
                
            }
            else if(count == 2){
                switch(r){
                    case 1:
                        s = "X" + s;
                        break;
                    case 2:
                        s = "XX" + s;
                        break;
                    case 3:
                        s = "XXX" + s;
                        break;
                    case 4:
                        s = "XL" + s;
                        break;
                    case 5:
                        s = "L" + s;
                        break;
                    case 6:
                        s = "LX" + s;
                        break;
                    case 7:
                        s = "LXX" + s;
                        break;
                    case 8:
                        s = "LXXX" + s;
                        break;
                    case 9:
                        s = "XC" + s;
                        break;
                    default:
                        break;
                }
                
            }
            
            else if(count == 3){
                switch(r){
                    case 1:
                        s = 'C' + s;
                        break;
                    case 2:
                        s = "CC" + s;
                        break;
                    case 3:
                        s = "CCC" + s;
                        break;
                    case 4:
                        s = "CD" + s;
                        break;
                    case 5:
                        s = "D" + s;
                        break;
                    case 6:
                        s = "DC" + s;
                        break;
                    case 7:
                        s = "DCC" + s;
                        break;
                    case 8:
                        s = "DCCC" + s;
                        break;
                    case 9:
                        s = "CM" + s;
                        break;
                    default:
                        break;
                }
                
            }
            else if(count == 4){
                switch(r){
                    case 1:
                        s = 'M' + s;
                        break;
                    case 2:
                        s = "MM" + s;
                        break;
                    case 3:
                        s = "MMM" + s;
                        break;
                    
                    default:
                        break;
                }
                
            }
        }
             return s;
    }
       
}