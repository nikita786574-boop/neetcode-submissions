class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left = 0
        med = 1
        right = len(nums) - 1
        res = []

        while left < med < right:
            while med < right:
                add = nums[left] + nums[right] + nums[med]
                if add > 0:
                    right -= 1
                elif add < 0:
                    med += 1
                else:
                    res.append((nums[left], nums[med], nums[right]))
                    right -= 1
            left += 1
            med = left + 1
            right = len(nums) - 1
        return list(set(res))