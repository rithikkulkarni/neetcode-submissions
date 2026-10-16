class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solution = []

        # for i in range(len(strs)):
        #     if strs[i] == "VISITED":
        #         continue
        #     curr = "".join(sorted(strs[i]))
        #     subsolution = []
        #     subsolution.append(strs[i])
        #     for j in range(i+1, len(strs)):
        #         if strs[j] == "VISITED":
        #             continue
        #         temp = "".join(sorted(strs[j]))
        #         if curr == temp:
        #             subsolution.append(strs[j])
        #             strs[j] = "VISITED"
        #     solution.append(subsolution)
        # return solution

        solution = []
        my_map = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            my_map[sortedS].append(s)
        return list(my_map.values())
                
        

            
        
