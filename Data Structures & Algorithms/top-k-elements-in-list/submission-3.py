class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] = hashmap[n] + 1
            else:
                hashmap[n] = 1

        solution = []
        
        for key, value in hashmap.items():
            solution.append([value, key])
        solution.sort()


        ret = []
        while len(ret) < k:
            ret.append(solution.pop()[1])
        return ret