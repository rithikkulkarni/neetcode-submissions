class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            mymap[sortedS].append(s)
        return list(mymap.values())
                
        

            
        
