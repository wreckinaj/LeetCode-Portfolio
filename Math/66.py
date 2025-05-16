'''
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most
significant to least significant in left-to-right order. The large integer does
not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        # Loop through all digits in reverse order like standard column addition
        for i in range(len(digits) - 1, -1, -1):
            # First case where we simply add one to our last digit
            if i == len(digits) - 1:
                # Start a carry if we get 9 + 1
                if digits[i] == 9:
                    carry = 1
                    digits[i] = 0
                    # Handle case for needing to add a digit
                    if i == 0:
                        digits.insert(0,1)
                # Otherwise, we are done
                else:
                    digits[i] += 1
            # For other digits where we are holding a carry
            elif carry == 1:
                # Keep the carry if current digit is 9
                if digits[i] == 9:
                    digits[i] = 0
                    # Case for needing to add a digit (list of all 9s)
                    if i == 0:
                        digits.insert(0, 1)
                # Add one, and we are done
                else:
                    digits[i] += 1
                    carry = 0
            # If we do not have a carry, it will never come back, so we can terminate
            # the loop early.
            else:
                break
        return digits