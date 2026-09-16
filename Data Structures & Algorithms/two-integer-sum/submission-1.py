class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary=dict()
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in dictionary:
                return [dictionary[complement], index]
            dictionary[nums[index]] = index