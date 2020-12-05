class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def lengthofLongestHere(s):
            l = 1
            cur = ""
            cur += s[0]
            for i in range(1, len(s)):
                if s[i] in cur:
                    return len(cur)
                else:
                    cur += s[i]
                
            return len(cur)
        if s == "":
            return 0
        l = 1
        temp = 1
        length = len(s)
        for i in range(length):
            temp = lengthofLongestHere(s[i:length])
            if temp > l:
                l = temp
        
        return l
