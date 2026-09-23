"""
LeetCode 283:移动零(Move Zeroes)

题目:把数组中的所有 0 移到末尾,同时保持非零元素的相对顺序(原地修改).

方法:同向双指针(快慢指针),O(n) 时间,O(1) 空间.

逻辑推导:
    slow 指针的含义 = "下一个非零元素应该放的位置".
    fast 指针负责遍历数组,遇到非零元素就和 slow 位置交换,然后 slow 前进.

    因为 slow 走过的位置都已经放好了非零元素,所以交换后:
    非零元素被逐步"搬到前面",0 被"挤到后面",最终所有 0 落到末尾.

    例子:[2, 3, 0, 7, ...]
      fast=0 遇到 2(非零)-> 和 slow=0 交换(原地)-> slow=1
      fast=1 遇到 3(非零)-> 和 slow=1 交换(原地)-> slow=2
      fast=2 遇到 0        -> 跳过,slow 停在 2(正好指向这个 0)
      fast=3 遇到 7(非零)-> 和 slow=2 交换 -> [2,3,7,0,...] -> slow=3
"""

from typing import List  # 注意:List 未使用(方法签名用的是内置 list[int]),模板残留


class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0                            # slow:下一个非零元素该放的位置
        for fast in range(len(nums)):       # fast:遍历探路
            if nums[fast] != 0:             # (1) 遇到非零
                # (2) 把非零元素搬到 slow 位置(0 被往后挤)
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1                   # (3) slow 前进一格
        return nums


if __name__ == "__main__":
    s1 = Solution()
    ans = s1.moveZeroes([2, 3, 0, 7, 3, 0, 11, 0, 15])
    print(ans)
