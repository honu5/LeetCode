class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Store the original number to compare later
        original = x
        reversed_num = 0
        
        while x > 0:
            # Get the last digit
            last_digit = x % 10
            # Build the reversed number
            reversed_num = reversed_num * 10 + last_digit
            # Remove the last digit from x
            x //= 10
        return original == reversed_num