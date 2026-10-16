class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        maxLeftHeight = 0
        maxRightHeight = 0
        for i in range(len(height)):
            if height[i] > maxLeftHeight:
                maxLeftHeight = height[i]
            maxLeft.append(maxLeftHeight)
        for j in range(len(height) - 1, -1, -1):
            if height[j] > maxRightHeight:
                maxRightHeight = height[j]
            maxRight.append(maxRightHeight)
        maxRight.reverse()

        solution = 0

        for k in range(len(height)):
            solution += min(maxLeft[k], maxRight[k]) - height[k]
        return solution
            