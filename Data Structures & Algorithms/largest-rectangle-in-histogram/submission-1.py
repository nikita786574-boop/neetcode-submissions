class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [0]
        min_left = [i for i in range(len(heights))]
        min_right = [i for i in range(len(heights))]
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                index = stack[-1]
                min_right[index] = i
                del stack[-1]
                if len(stack) == 0:
                    break
            
            if len(stack) != 0 and heights[i] >= heights[stack[-1]]:
                if heights[i] == heights[stack[-1]]:
                    min_left[i] = min_left[stack[-1]] 
                else:
                    min_left[i] = stack[-1]
            stack.append(i)
        max_square = 0
        for i in range(len(heights)):
            
            if min_right[i] == i:
                right = len(heights)
            else:
                right = min_right[i] 
            if min_left[i] == i:
                left = -1
            else:
                left = min_left[i]
            diff = right - left
            max_square = max(max_square, heights[i] * (diff - 1))
        return max_square