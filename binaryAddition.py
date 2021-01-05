class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ey = int(a, 2)
        bee = int(b, 2)
        
        see = ey + bee
        return "{0:b}".format(see)
        
        
