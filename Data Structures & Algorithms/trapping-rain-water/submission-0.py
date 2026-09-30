class Solution:
    def trap(self, height: list[int]) -> int:
        # Найти глобальный максимум. Разрезать и два раза сделать.
        global_max_index = 0
        max_item = max(height)
        for i in range(len(height)):
            if height[i] == max_item:
                global_max_index = i
                break
        height1 = [0]+height[:global_max_index + 1]
        height2 = height[global_max_index:]+[0]
        left = 0
        right = 0
        search = True
        height = height1
        n = len(height)
        amount = 0

        while left <= n - 3:
            if height[left] == 0:
                left += 1
                continue
            right = left + 1
            # Найти первый, который не меньше height[left]
            # или максимальный их тех, что ниже его
            max_right = height[right]
            index_right = right
            while right < n - 1 and height[right] < height[left]:
                right += 1
                if height[right] >= max_right:
                    max_right = height[right]
                    index_right = right
            min_height = min(height[left], max_right)
            for between in range(left+1, index_right):
                amount += min_height - height[between]
            left = index_right 
        left = 0
        right = 0
        search = True
        height = height2[::-1]
        n = len(height)

        while left <= n - 3:
            if height[left] == 0:
                left += 1
                continue
            right = left + 1
            # Найти первый, который не меньше height[left]
            # или максимальный их тех, что ниже его
            max_right = height[right]
            index_right = right
            while right < n - 1 and height[right] < height[left]:
                right += 1
                if height[right] >= max_right:
                    max_right = height[right]
                    index_right = right
            min_height = min(height[left], max_right)
            for between in range(left+1, index_right):
                amount += min_height - height[between]
            left = index_right 
        return amount