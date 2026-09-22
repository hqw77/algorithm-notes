class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups={}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())




if __name__ == "__main__":
    s1 = Solution()
    ans = s1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ans)