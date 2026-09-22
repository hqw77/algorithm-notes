

d = {}
d['a'] = 1
d.get('a',0)

print(d)
ans1 = 'a' in d 
print(ans1)

s = set()
s.add(1)
ans = 1 in s 
print(ans)

from collections import Counter
c = Counter([1,1,2,3])
ans2=c[1]
print(ans2)