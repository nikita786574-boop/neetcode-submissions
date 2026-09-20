class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        prefixes = [0 for i in range(sz)]
        postfixes = [0 for i in range(sz)]
        prefixes[-1] = nums[-1]
        postfixes[0] = nums[0]
        for i in range(1, sz-1):
            prefixes[sz-i-1] = prefixes[sz-i]*nums[sz-i-1]
            postfixes[i] = postfixes[i-1] * nums[i]
        result = [0 for i in range(sz)]
        result[0] = prefixes[1]
        result[-1] = postfixes[-2]
        for i in range(1, sz-1):
            result[i] = postfixes[i-1]*prefixes[i+1]
        return result