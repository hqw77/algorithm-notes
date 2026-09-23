"""
LeetCode 11:盛最多水的容器(Container With Most Water)

题目:给一个数组 height,每个元素是一根柱子的高度.任选两根柱子,
      它们和 x 轴围成的容器能装多少水?求"最大"装水量.

方法:相向双指针(左右夹逼),O(n) 时间,O(1) 空间.

数学推导(核心):
    面积 = 宽 * 高 = (right - left) * min(height[left], height[right])

    装水量由"较矮"的那根柱子决定(木桶原理).

    为什么每一步都移动较矮的一边?
      - 移动较高的一边 -> 宽度必然变小,而高度最多还是矮边那么高(甚至更低),
        面积一定不会变大,可以直接排除.
      - 移动较矮的一边 -> 宽度虽然变小,但可能遇到更高的柱子,面积有机会变大.
    所以每次移动矮边,相当于"每步排除一个不可能成为答案的柱子",总共 O(n).
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1   # 左右指针:从"最宽"的两端开始
        max_area = 0
        while left < right:
            width = right - left                   # (1) 当前宽度
            h = min(height[left], height[right])   # (2) 高度由矮边决定(木桶原理)
            area = width * h                       # (3) 面积 = 宽 * 高
            max_area = max(max_area, area)         # (4) 更新最大面积

            # (5) 移动较矮的一边:矮边是限制因素,移动它才可能让面积变大
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    s1 = Solution()
    ans = s1.maxArea([2, 3, 0, 7, 3, 0, 11, 0, 15])
    print(ans)
