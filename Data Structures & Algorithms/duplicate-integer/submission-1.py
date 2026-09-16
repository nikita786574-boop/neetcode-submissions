class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dictionary = dict()
        for i in range(n):
            item = dictionary.setdefault(nums[i], i)
            if item != i:
                return True
        return False