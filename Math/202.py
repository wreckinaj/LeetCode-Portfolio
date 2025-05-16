'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares
of its digits.

Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        # Use a set to keep track of what numbers we run into
        num_set.add(n)
        # Terminate when n = 1
        while n != 1:
            # Find the sum to replace n
            temp = 0
            # Use to make sure we square each digit
            digit = 10
            while n != 0:
                # Take the mod and divide it, then square the digit
                temp += ((n % digit) // (digit // 10))  ** 2
                # Prepare for the next digit
                n -= (n % digit)
                digit *= 10
            # Replace n with the new sum
            n = temp
            # If n is already in the set, we have ran into a cycle, and the parameter
            # n is not a happy number
            if n in num_set:
                return False
            num_set.add(n)
        return True