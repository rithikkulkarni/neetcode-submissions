class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        leftTotal = 1
        rightTotal = 1

        for i in range(len(nums)):
            leftTotal *= nums[i]
            left.append(leftTotal)
        for i in range(len(nums) - 1, 0, -1):
            rightTotal *= nums[i]
            right.append(rightTotal)
        right.reverse()

        output = []

        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output