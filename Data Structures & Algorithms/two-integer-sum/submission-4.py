class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        result = []

        for i in range(len(nums)):
            if nums[i] in hashmap:
                result.append(hashmap[nums[i]])
                result.append(i)
                return result
            hashmap[target - nums[i]] = i