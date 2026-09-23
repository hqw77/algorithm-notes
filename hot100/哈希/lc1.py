"""
LeetCode 1:两数之和(Two Sum)

题目:给数组 nums 和目标 target,找出和为 target 的两个数的"下标".
      假设只有一个答案,且同一元素不能重复使用.

方法:哈希表(边遍历边查),O(n) 时间,O(n) 空间.

逻辑推导:
    要找 nums[i] + nums[j] = target,即对当前元素 x,找是否存在 target - x.
    用字典 seen 记录"值 -> 下标":遍历时先查 target - x 是否出现过,
    出现过就找到答案;没出现过就把当前 (值, 下标) 存进去.

    为什么"边遍历边存"而不是先全部存好?
      因为答案的两个数,后遍历到的那个能立刻查到先遍历到的那个;
      如果先全部存好,可能误用同一个元素两次.

    例子:nums=[2,7,11,15], target=9
      i=0, x=2, 找 7 -> 不在 seen,存 {2:0}
      i=1, x=7, 找 2 -> 在!返回 [0,1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        seen = {}                          # 值 -> 下标
        for i, x in enumerate(nums):
            if target - x in seen:         # (1) 查"另一半"是否出现过
                return [seen[target - x], i]
            seen[x] = i                    # (2) 没找到,把当前值存进去
        return []


if __name__ == "__main__":
    s1 = Solution()
    ans = s1.twoSum([2, 7, 11, 15], 9)
    print(ans)
