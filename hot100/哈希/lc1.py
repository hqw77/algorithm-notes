from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int) -> list[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target -x in seen:
                return [seen[target-x],i]
            seen[x]=i
        return []



if __name__ == "__main__":
    s1 = Solution()
    ans = s1.twoSum([2,7,11,15],9)
    print(ans)
