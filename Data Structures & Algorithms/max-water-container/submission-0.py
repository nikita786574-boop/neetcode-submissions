class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left_max = 0
        left = 0 
        right = len(height) - 1
        right_max = height[-1]
        # Справа будет указатель. Посчитаем кол-во
        # Воды для текущего левого и потом двигаем правый.
        # Нам важно только те, что больше чем максимальный правый.
        # И левый тоже. Двигаем, но останавливаеся только там,
        # где больше, чем уже было. И для него снова пробегаемся правым
        while left < right:
            width = right - left
            height_iter = min(height[left], height[right])
            max_water = max(max_water, width * height_iter)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_water