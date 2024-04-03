class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = []
        prefix_products = [1, nums[0]]
        postfix_products = [1] * n
        postfix_products[-1] = 1
        postfix_products[-2] = nums[-1]

        for i in range(n):
            if i<=1:
                continue
            prefix_products.append(nums[i-1] * prefix_products[i-1])

        for i in range(n):
            if i<=1:
                continue
            postfix_products[-i-1] = nums[-i] * postfix_products[-i]

        print(prefix_products)
        print(postfix_products)

        for i in range(n):
            products.append(prefix_products[i] * postfix_products[i])
        return products


        
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution().productExceptSelf(nums)
    print(solution)

         
