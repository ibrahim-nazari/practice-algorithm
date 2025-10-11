class Solution:
    def maxRectangle(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        height = [0] * m
        max_area = 0

        for i in range(n):
            # Build the histogram
            for j in range(m):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            
            # Calculate max area for this histogram
            max_area = max(max_area, self.largestRectangleArea(height))
        
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # sentinel to clear stack at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()
        return max_area


solution=Solution()
mat = [
  [0, 1, 1, 0],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 0, 0]
]

res=solution.maxRectangle(mat)
print(res)
