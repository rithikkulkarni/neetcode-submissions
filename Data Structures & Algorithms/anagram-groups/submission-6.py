class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # "aht" -> ["hat"]
        # "act" -> ["act", "cat"]
        # "post" -> ["stop", "pots", "tops"]

        map = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            map[temp].append(s)
        
        return list(map.values())