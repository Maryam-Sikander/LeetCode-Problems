class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[nums[i]] = i
            