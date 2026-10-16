class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()

        for i in range(len(nums)):
            if nums[i] in my_map:
                solution = []
                solution.append(my_map[nums[i]])
                solution.append(i)
                return solution
            else:
                my_map[target - nums[i]] = i