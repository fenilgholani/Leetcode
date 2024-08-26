class Solution:
    def reformat(self, s: str) -> str:
        
        char = []
        countc = 0
        countd = 0
        digit = []

        for ch in s:

            if ch.isdigit():
                countd += 1
                digit.append(ch)
            else:
                countc += 1
                char.append(ch)
        
        if (countd > countc and countd - 1 != countc)  or (countc > countd and countc - 1 != countd):
            return ""

        ans = ""

        if countd > countc:
            ans = digit.pop(0)
        
        elif countd < countc:
            ans = char.pop(0)

        while digit != []:
            if countc > countd:
                ans += digit.pop(0) + char.pop(0)
            else:
                ans += char.pop(0) + digit.pop(0)
        return ans
        