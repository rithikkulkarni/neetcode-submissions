class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for s in strs:
            normalized = ''.join(sorted(s))
            map[normalized].append(s)

        return list(map.values())


        
        
        
        
        
        
        
        