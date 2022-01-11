import sys

n,k=map(int,sys.stdin.readline().split())
s=""
for i in range(n+1):
    s+=str(i)
print(s[k])
