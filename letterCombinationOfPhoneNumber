class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def findLetter(digit):
            if digit == '2':
                return ["a", "b", "c"]
            elif digit == '3':
                return ["d", "e", "f"]
            elif digit == '4':
                return ["g", "h", "i"]
            elif digit == '5':
                return ["j", "k", "l"]
            elif digit == '6':
                return ["m", "n", "o"]
            elif digit == '7':
                return ["p", "q", "r", "s"]
            elif digit == '8':
                return ["t", "u", "v"]
            else:
                return ["w", "x", "y", "z"]
            
        
        currOut = []
        for digit in digits:
            if currOut == []:
                currOut = findLetter(digit)
            else:
                newCurrOut = []
                for item in currOut:
                    for letter in findLetter(digit):
                        newCurrOut.append(item + letter)
                currOut = newCurrOut
        return currOut
