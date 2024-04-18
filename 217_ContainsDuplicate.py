class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = 0


        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True
        return False
            

        
if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    solution = Solution().containsDuplicate(nums)
    print(solution)
