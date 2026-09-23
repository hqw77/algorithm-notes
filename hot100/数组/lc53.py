"""
LeetCode 53:最大子数组和(Maximum Subarray)

题目:给整数数组 nums,找出"和最大的连续子数组",返回最大和.

方法:动态规划(Kadane 算法),O(n) 时间,O(n) 空间(可优化到 O(1)).

数学推导:
    定义 dp[i] = 以 nums[i] 结尾的连续子数组的最大和.

    对第 i 个元素,只有两种选择:
      1. 接到前面的子数组后面:dp[i-1] + nums[i]
      2. 自己单独开始:nums[i]

    怎么选?取决于 dp[i-1] 的正负:
      - 若 dp[i-1] >= 0,前面的和是"正贡献",接上更好 -> dp[i] = dp[i-1] + nums[i]
      - 若 dp[i-1] <  0,前面的和是"负拖累",不如重新开始 -> dp[i] = nums[i]

    即状态转移方程:dp[i] = max(nums[i], dp[i-1] + nums[i])

    最终答案 = max(dp),因为最大子数组一定以某个位置结尾.
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        size = len(nums)
        if size == 0:              # 空数组边界
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]            # (1) 初始化:以第一个元素结尾的最大和就是它自己
        for i in range(1, size):
            if dp[i - 1] >= 0:              # (2) 前面的和是正贡献
                dp[i] = dp[i - 1] + nums[i]  # 接上前面
            else:                            # (3) 前面的和是负拖累
                dp[i] = nums[i]              # 重新开始
        return max(dp)              # (4) 所有结尾位置里取最大


if __name__ == "__main__":
    s = Solution()
    # 注意:测试输入里 `1-3` 是笔误(Python 会算成 -2),原题例应为 `1,-3`
    ans = s.maxSubArray([-2, 1, - 3, 4, -1, 2, 1, -5, 4])
    print(ans)
