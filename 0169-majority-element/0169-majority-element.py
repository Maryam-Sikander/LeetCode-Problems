class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = len(nums)
        return nums[count//2]