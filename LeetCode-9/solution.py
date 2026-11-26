class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        original = x
        while (x > 0):
            lastdigit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + lastdigit
        return reversed_num == original

    

    
    

        
        
        

        
        