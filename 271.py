class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        return encoded_str


    def decode(self, s: str) -> list[str]:
        decoded_strs = []
        i = 0
        str_len = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+str_len])
            i = j + 1 + str_len
            

        return decoded_strs



if __name__ == "__main__":
    strs = ["hello", "^!%@&#%!@*&^!@)#)asdac", "12#", ""]
    s = "5#hello22#^!%@&#%!@*&^!@)#)asdac3#12#0#"
    print(s)
    print(Solution().decode(s))
    #solution = Solution().decode(Solution().encode(strs=strs))
    #print(solution)

        
