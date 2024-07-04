class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        duplicate_set = set()        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_element = nums[i] + nums[j] + nums[k]
                if sum_element == target:
                    duplicate_set.add((nums[i], nums[j], nums[k]))
                    j+= 1
                    k -= 1
                elif sum_element < target:
                    j += 1
                else:
                    k -= 1
        return list(duplicate_set)
                