class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()

        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        sort = []
        for n, count in map.items():
            sort.append([count, n])
        sort.sort()

        solution = []
        while len(solution) < k:
            solution.append(sort.pop()[1])
        return solution