class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num  = max(nums)
        for i in nums:
            if i != max_num:
                if max_num < i * 2:
                    return - 1
                    break
        return nums.index(max_num)