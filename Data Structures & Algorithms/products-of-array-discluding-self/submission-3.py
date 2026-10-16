class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftList = []
        rightList = []

        left = right = 1

        leftList.append(1)
        for i in range(0, len(nums) - 1):
            left *= nums[i]
            leftList.append(left)
        
        rightList.append(1)
        for i in range(len(nums) - 1, 0, -1):
            right *= nums[i]
            rightList.append(right)
        rightList.reverse()

        solution = []

        for i in range(len(leftList)):
            solution.append(leftList[i] * rightList[i])
        return solution


