from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_dict = defaultdict(int)
        length = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                product = nums[i] * nums[j]
                if product in prod_dict:
                    length += prod_dict[product]
                prod_dict[product] += 1
        return length * 8


        return length