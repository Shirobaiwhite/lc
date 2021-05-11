class Solution:
        
    def romanToInt(self, s: str) -> int:
        def isFourNine(s):
            firstTwo = s[:2]
            if firstTwo == 'IV':
                return 4
            elif firstTwo == 'IX':
                return 9
            elif firstTwo == 'XL':
                return 40
            elif firstTwo == 'XC':
                return 90
            elif firstTwo == 'CD':
                return 400
            elif firstTwo == 'CM':
                return 900
            else:
                return 0
            
        myInt = 0
        pos = 0
        while pos < len(s):
            if pos != len(s) - 1:
                check = isFourNine(s[pos:pos+2])
                if check != 0:
                    myInt += check
                    pos += 2
                    if pos >= len(s):
                        break
                    else:
                        continue
            if s[pos] == 'M':
                myInt += 1000
                pos += 1
            elif s[pos] == 'D':
                myInt += 500
                pos += 1
            elif s[pos] == 'C':
                myInt += 100
                pos += 1
            elif s[pos] == 'L':
                myInt += 50
                pos += 1
            elif s[pos] == 'X':
                myInt += 10
                pos += 1
            elif s[pos] == 'V':
                myInt += 5
                pos += 1
            else:
                myInt += 1
                pos += 1
        return myInt
        
                
            

            
        
