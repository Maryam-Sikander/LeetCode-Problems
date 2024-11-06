class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num_sort = sorted(nums)
        sum_elements = 0
        # return sum of min_list
        for i in num_sort[::2]:
            sum_elements += min(i, i+1)
        return sum_elements



    