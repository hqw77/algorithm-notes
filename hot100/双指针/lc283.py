from typing import List 
class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow+=1
        return nums

if __name__ == "__main__":
    s1 = Solution()
    ans = s1.moveZeroes([2,3,0,7,3,0,11,0,15])
    print(ans)