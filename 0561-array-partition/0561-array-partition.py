class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num_sort = sorted(nums)
        # pairs using list comprehension
        pairs = [(num_sort[i], num_sort[i+1]) for i in range(0, len(nums), 2)]

        # check for minimum element
        min_list = [min(i) for i in pairs]

        # return sum of min_list
        return sum(min_list)