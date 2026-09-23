class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        #used = set()
        max_length = 0
        for item in unique:
            current_length = 0
            if item - 1 not in unique:#item not in used and 
                while item in unique:
                    current_length += 1
                    max_length = max(max_length, current_length)
                    item += 1
                    #used.add(item)
        return max_length