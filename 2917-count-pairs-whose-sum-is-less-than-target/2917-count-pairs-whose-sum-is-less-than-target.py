class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        pairs = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                pairs += (right - left)
                left += 1
            else:
                right -= 1
        return pairs




        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) < target:
        #             pairs += 1
        # return pairs