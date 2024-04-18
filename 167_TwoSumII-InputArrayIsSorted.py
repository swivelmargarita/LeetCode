class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            if sum > target:
                r -= 1
            else:
                l += 1
        return []

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    numbers = [2,3,4]
    target = 6
    numbers = [-1,0]
    target = -1
    print(Solution().twoSum(numbers, target))
