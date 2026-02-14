class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = num  &  0xffffffff
        
        return format(num , 'x')