class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        string = ""
        sizes = []
        for s in strs:
            sizes.append(len(s))
            string = string + s

        encoded = ""
        for size in sizes:
            encoded = encoded + str(size) + ','
        encoded = encoded + '#' + string
        return encoded
        

    def decode(self, s: str) -> List[str]:
        solution = []
        if s == "":
            return []

        i = 0
        sizes = []
        temp_size = ""
        while s[i] != '#':
            
            if s[i].isdigit():
                temp_size = temp_size + s[i]
            else:
                value = int(temp_size)
                temp_size = ""
                sizes.append(value)
            i = i + 1
        
        curr = i + 1
        for size in sizes:
            decoded_string = ""
            for k in range(curr, curr + size):
                decoded_string = decoded_string + s[k]
            solution.append(decoded_string)
            curr = curr + size

        return solution
        


