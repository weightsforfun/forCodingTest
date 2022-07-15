import sys
n,m,k=map(int,sys.stdin.readline().split())

woman=n//2
man=m
max_team=min(woman,man)

while(m+n-(max_team*3)<k):
    max_team-=1


if(max_team>=0):
    print(max_team)
else:
    print(0)