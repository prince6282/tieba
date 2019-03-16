#1 等号比较的是value，
#2 is比较的是id

#强调：
#1. id相同，意味着type和value必定相同
#2. value相同type肯定相同，但id可能不同,如下
x='Info Egon:18'
y='Info Egon:18'

id(x)
id(y)

print(x == y)

print(x is y)
