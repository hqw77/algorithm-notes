from typing import List
class Solution:
    # 暴力解法
    def longestConsecutive(self, nums: list[int]) -> int:
        for x in nums: 
            length=1
            while x+1 in nums:
                x+=1
                length+=1
            return length

    # 哈希
    def longestConsecutive1(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for x in num_set:
            if x-1 not in num_set:
                cur = x
                length = 1
                while cur+1 in num_set:
                    cur+=1
                    length+=1
                longest = max(longest,length)
        return longest






if __name__ == "__main__":
    s1 = Solution()
    ans = s1.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    ans1 = s1.longestConsecutive1([0,3,7,2,5,8,4,6,0,1])
    print(ans)
    print(ans1)