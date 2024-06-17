'''
5
1 2 3 4 5
o/p:[13,9,3,5,15]'''
n=int(input())
a=list(map(int,input().split()))
ts=0
ls=0#left_sum
rs=0#right_sum
cs=0#current sum
ans=[]
#calculating sum
for i in a:
    ts+=i
#left to right difference
for i in a:
    ls+=i
    rs=ts-ls
    cs=abs(rs-ls)
    ans.append(cs)
print(ans)



