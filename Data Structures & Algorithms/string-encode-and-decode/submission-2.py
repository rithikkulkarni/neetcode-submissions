# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         string = ""
#         sizes = []
#         for s in strs:
#             sizes.append(len(s))
#             string = string + s

#         encoded = ""
#         for size in sizes:
#             encoded = encoded + str(size) + ','
#         encoded = encoded + '#' + string
#         return encoded
        

#     def decode(self, s: str) -> List[str]:
#         solution = []
#         if s == "":
#             return solution

#         i = 0
#         sizes = []
#         temp_size = ""
#         while s[i] != '#':
            
#             if s[i].isdigit():
#                 temp_size = temp_size.join(s[i])
#             else:
#                 value = int(temp_size)
#                 sizes.append(value)
#             i = i + 1
        
#         curr = i + 1
#         for size in sizes:
#             decoded_string = ""
#             for k in range(curr, curr + size):
#                 decoded_string = decoded_string + s[k]
#             solution.append(decoded_string)
#             curr = curr + size

#         return solution
        


class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res