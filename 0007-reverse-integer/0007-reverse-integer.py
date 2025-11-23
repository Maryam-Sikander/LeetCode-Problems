class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        is_negative = x < 0
        temp = abs(x)
        while temp > 0:
            digit = temp % 10
            reverse_num = reverse_num * 10 + digit
            temp = temp // 10
        if reverse_num.bit_length() < 32:
            if is_negative:
                return -reverse_num
            else: 
                return reverse_num 
        else:
            return 0