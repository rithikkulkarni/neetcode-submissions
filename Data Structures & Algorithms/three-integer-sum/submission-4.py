class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int):
            solutions = []
            left = 0
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    temp = []
                    temp.append(nums[left])
                    temp.append(nums[right])
                    solutions.append(temp)
                    left += 1
            return solutions

        final_solution = []
        seenset = set()
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in seenset:
                seenset.add(nums[i])
            else:
                continue
            subsolution = []
            subsolution.append(nums[i])
            var = twoSum(nums[i+1:], -1*nums[i])
            for pair in var:
                triplet = subsolution + pair
                if len(triplet) == 3 and triplet not in final_solution:
                    final_solution.append(triplet)
        return final_solution

                        