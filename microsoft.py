
def rev(s):
   
    lst_word = s.split(' ')
    ans = ""
     
    for i in range(len(lst_word)):
        
        temp_word = ""
        rev_word = ""
         
        for c in lst_word[i]:
             
            if not c.isalpha():
                rev_word += temp_word[::-1] + c
                temp_word = ""
            else:
                temp_word += c
             
        ans += rev_word + temp_word[::-1] + " "

    return ans
 
 
s = 'The quick, br456own 125 foxes jumps over the lazy dog!'
 
print(rev(s))