import sys
input=sys.stdin.readline
 
n=int(input())

days=[]

for i in range(n):
    days.append(list(map(int,input().split(" "))))