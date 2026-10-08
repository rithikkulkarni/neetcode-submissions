class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i in range(len(nums)):
            if nums[i] in map:
                solution = []
                solution.append(map[nums[i]])
                solution.append(i)
                return solution
            else:
                map[target - nums[i]] = i
        