'''
lc167.两数之和 II（有序数组）
在升序数组中找到两个数，使它们的和等于 target，返回索引。
'''

from typing import List

# 暴力解法（O（n^2））
class Solution1:
    def twoSum(self,nums:List[int],target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# 双指针（O（n））
class Solution2:
    def twoSum(self,nums:List[int],target:int) -> list[int]:
        left,rigth=0,len(nums)-1
        while left < rigth:
            if nums[left]+nums[rigth]==target:
                return [left+1,rigth+1]
            elif nums[left]+nums[rigth] < target:
                left+=1
            else:
                rigth-=1
        return []
        



if __name__ == "__main__":
    s1 = Solution1()
    ans = s1.twoSum([2,7,11,15],9)
    print(ans)

    s2 = Solution2()
    ans2 = s2.twoSum([2,7,11,15],9)
    print(ans2)