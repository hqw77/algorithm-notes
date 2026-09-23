"""
哈希表基础操作练习(Python)

演示三种最常用的哈希结构:
  1. dict    -- 键值对,用于"存映射""计数"
  2. set     -- 集合,用于"判存在""去重"
  3. Counter -- 计数器快捷写法(本质是 dict 子类)

核心:查找 / 插入 / 删除都是平均 O(1),用空间换时间.
"""

# (1) dict:存键值对
d = {}
d['a'] = 1
d.get('a', 0)   # 取值,键不存在时返回默认值 0(避免 KeyError)

print(d)
ans1 = 'a' in d  # 判断键是否存在,O(1)
print(ans1)

# (2) set:只存键,判存在 / 去重
s = set()
s.add(1)
ans = 1 in s     # O(1)
print(ans)

# (3) Counter:统计频率
from collections import Counter
c = Counter([1, 1, 2, 3])
ans2 = c[1]      # 元素 1 出现了 2 次
print(ans2)
