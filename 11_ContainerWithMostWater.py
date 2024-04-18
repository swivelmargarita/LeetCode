class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            max_water = max(min(height[l], height[r]) * (r-l), max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water

if __name__ == "__main__":
    height = [5,5,12,1,9,5,8,13,2,9]
    print(Solution().maxArea(height))
