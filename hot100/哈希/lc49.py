"""
LeetCode 49:字母异位词分组(Group Anagrams)

题目:把"字母相同,排列不同"的字符串分到同一组.
      例:["eat","tea","tan","ate","nat","bat"]
        -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]

方法:排序 + 哈希分组,O(n*k log k).

逻辑推导:
    异位词的本质是"字母计数相同",而"计数相同"等价于"排序后字符串相同".
    例如 "eat" 和 "tea" 排序后都是 "aet".
    所以用"排序后的字符串"作为 key,把原始字符串归到同一个组里.

    进阶:key 也可用"26 个字母的计数元组",把排序的 k log k 降到 k(面试提一句即可).
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}                        # key(排序后) -> 这一组的字符串列表
        for s in strs:
            key = "".join(sorted(s))       # (1) 排序后作为 key(异位词排序后相同)
            if key not in groups:          # (2) 新 key 先建一个空列表
                groups[key] = []
            groups[key].append(s)          # (3) 把原字符串归入该组
        return list(groups.values())       # (4) 返回所有组


if __name__ == "__main__":
    s1 = Solution()
    ans = s1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)
