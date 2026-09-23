"""
LeetCode 128:最长连续序列(Longest Consecutive Sequence)

题目:给未排序的整数数组 nums,找出"最长连续序列"的长度(要求 O(n)).

方法:哈希集合 + 只从"序列起点"开始数,O(n) 时间,O(n) 空间.

逻辑推导:
    暴力思路是对每个数 x 往后数 x+1, x+2, ... 能连多长,但那样每个序列
    会被重复数很多次(例如 [1,2,3,4] 会被数 4 次),变成 O(n^2).

    关键优化:只从"起点"开始数.一个数 x 是"起点"当且仅当 x-1 不在集合里.
    这样每个连续序列只会被数一次,总时间 O(n).
"""

from typing import List  # 注意:List 未使用(方法签名用的是内置 list[int]),模板残留


class Solution:
    # ---- 方法一:暴力(O(n^2)),仅示意思路 ----
    def longestConsecutive(self, nums: list[int]) -> int:
        for x in nums:
            length = 1
            while x + 1 in nums:   # 对 list 的 `in` 是 O(n),所以整体 O(n^2)
                x += 1
                length += 1
            return length
        # 注意:上面的 return 在 for 循环里,实际只返回"第一个数"的连续长度.
        # 这是暴力思路的简化示意(未对所有起点取 max),完整做法见方法二.

    # ---- 方法二:哈希集合 + 只从起点数(O(n)),推荐 ----
    def longestConsecutive1(self, nums: list[int]) -> int:
        num_set = set(nums)            # (1) 先去重,之后 O(1) 判存在
        longest = 0
        for x in num_set:
            if x - 1 not in num_set:   # (2) 只有"起点"(x-1 不存在)才往下数
                cur = x
                length = 1
                while cur + 1 in num_set:   # (3) 往后数连续
                    cur += 1
                    length += 1
                longest = max(longest, length)   # (4) 更新最长
        return longest


if __name__ == "__main__":
    s1 = Solution()
    ans = s1.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    ans1 = s1.longestConsecutive1([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(ans)
    print(ans1)
