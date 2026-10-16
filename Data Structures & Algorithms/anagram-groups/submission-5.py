class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        my_map = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            my_map[sortedS].append(s)
        return list(my_map.values())
                
        

            
        
