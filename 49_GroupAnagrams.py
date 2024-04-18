from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)

        return list(groups.values())
                

if __name__ == "__main__":
    strs = ['']
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(strs)
    solution = Solution().groupAnagrams(strs=strs)
    print(solution)

        
