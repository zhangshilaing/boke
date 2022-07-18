# 集合运算
set1={123,'中国',456}
set2={123,'USA','Japan'}

# 差集: 一个集合中包含且另一个集合中不包含的元素形成的集合
print(set1-set2) # {456, '中国'}
print(set1.difference(set2)) # {'中国', 456}

# 并集:一个集合和另一个集合合并成一个新的集合
print(set1 | set2) # {'Japan', 456, 123, 'USA', '中国'}
print(set1.union(set2)) # {'中国', 456, 'Japan', 123, 'USA'}

# 交集：两个集合均包含的元素形成的集合
print(set1 & set2) # {123}
print(set1.intersection(set2)) # {123}

# 差异集:两个集合中不同时包含的元素形成的集合
print(set1 ^ set2) # {'USA', 456, 'Japan', '中国'}
print(set1.symmetric_difference(set2)) # {'USA', 456, 'Japan', '中国'}

