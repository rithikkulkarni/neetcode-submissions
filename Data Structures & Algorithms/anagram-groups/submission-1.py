class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for s in strs:
            normalized = ''.join(sorted(s))
            map[normalized].append(s)

        solution = []
        
        for key in map:
            solution.append(map[key])
        
        return solution


        
        
        
        
        
        
        
        