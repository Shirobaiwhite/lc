class Solution:
    def climbStairs(self, n: int) -> int:
        def fibo(num):
            if num == 1:
                return 1
            elif num == 2:
                return 2
            else:
                return fibo(num - 1) + fibo(num - 2)
            
        return fibo(n)
