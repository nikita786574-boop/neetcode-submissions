class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = len(nums) // 2
        left = 0
        right = len(nums)
        while nums[index] != target:
            if nums[index] < target:
                left = index + 1
                index = left + (right-left)//2
                if left == right:
                    return -1
            else:
                right = index
                index = left + (right - left) // 2
                if left == right:
                    return -1
        return index