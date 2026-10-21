class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list)

        for s in strs:
            mymap["".join(sorted(s))].append(s)
        return list(mymap.values())