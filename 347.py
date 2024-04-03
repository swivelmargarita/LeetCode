from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        k_frequent = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        k_frequent = sorted(counts, key=counts.get, reverse=True)[:k]
        return k_frequent


        
if __name__ == "__main__":
    nums = [1,1,2,2,2,3,3,3,3,3,5]
    nums = [1]
    k = 1
    solution = Solution().topKFrequent(nums, k)
    print(solution)

        
