class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = max(nums)
        for i in range(len(nums)):
            if nums[i] == peak:
                return i