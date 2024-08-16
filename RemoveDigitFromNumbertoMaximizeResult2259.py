class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        maxi = 0

        for index in range(len(number)):

            if number[index] == str(digit):
                if maxi < int(number[:index] + number[index+1:]):
                    maxi = int(number[:index] + number[index+1:])
        
        return str(maxi)