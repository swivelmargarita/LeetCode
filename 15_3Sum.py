class Solution:
    def threeSum_wonky(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        three_sums = set()
        l = 0
        while l < n - 2:
            m = l + 1
            r = n - 1
            while m < r:
                three_sum = nums[l] + nums[m] + nums[r]
                if three_sum == 0:
                    three_sums.add(tuple([nums[l], nums[m], nums[r]]))
                    if r > m:
                        r -= 1
                    else:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    m += 1
            l += 1
        return [list(t) for t in three_sums]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        three_sums = []
        for i  in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    three_sums.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return three_sums

if __name__ == "__main__":
        nums = [-1,0,1,2,-1,-4]
        nums = [-1, 0, 1, 0, -9, -9, 1, 2, -1, 9, 2, -1, -4]
        print(Solution().threeSum(nums))


