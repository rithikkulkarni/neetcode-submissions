class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        
        for n in nums:
            if n in hashmap:
                hashmap[n] = hashmap[n] + 1
            else:
                hashmap[n] = 1

        arr = []
        
        for key, value in hashmap.items():
            arr.append([value, key])
        arr.sort()

        solution = []

        while len(solution) < k:
            solution.append(arr.pop()[1])
        
        return solution
