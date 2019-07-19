#python如何实现动态规划算法寻找最优匹配子串？
#题，譬如现在有一串字符串s1=“agtcgtaatgc”,想将另一个字符串s2="cgaa"比对到s1上，
#可以看到s2并非完全比对到s1上面，其中是有一个错配的。现在我要实现的就是寻找s2比对到s1上面的错配最少的位点。

import difflib

s1='agtcgtaatgc'

s2="cgaa"

mch=difflib.SequenceMatcher(a=s1,b=s2)

m=mch.find_longest_match(0,len(s1),0,len(s2))

print(s1[m.a:m.a+m.size],s2[m.b:m.b+m.size])

#cg cg




SequenceMatcher(None, "AAAA", "AACA").get_matching_blocks()
#[Match(a=0, b=0, size=2), Match(a=2, b=3, size=1), Match(a=4, b=4, size=0)]

SequenceMatcher(None, "AGGCGAAG", "AGCGATAG").find_longest_match(0, 8, 0, 8)
#Match(a=2, b=1, size=4)

SequenceMatcher(None, "AGGCGAAG", "AGCGATAG").ratio()
#0.875
