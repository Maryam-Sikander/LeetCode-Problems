class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        for j in nums:
            if j == i:
                i += 1
        return i