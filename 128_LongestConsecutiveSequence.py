class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return len(nums)

        longest_sequence = 1
        nums_set = set(nums)
        for num in nums_set:
            if num - 1  in nums_set:
                continue
            else:
                next_seq = num + 1
                curr_longest_sequence = 1
                while next_seq in nums_set:
                    curr_longest_sequence += 1
                    next_seq += 1
                if curr_longest_sequence > longest_sequence:
                    longest_sequence = curr_longest_sequence
        return longest_sequence

         
        

if __name__ == "__main__":
    nums = [3, 69, 4, 1, 422, 421, 70, 420, 2, 419, 0]
    print(Solution().longestConsecutive(nums))

        
