class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer <= right_pointer:
            add = numbers[left_pointer] + numbers[right_pointer]
            if add == target:
                return [left_pointer + 1, right_pointer + 1]
            if add < target:
                left_pointer += 1
            else:
                right_pointer -= 1