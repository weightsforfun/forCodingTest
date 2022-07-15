import sys

s=sys.stdin.readline().strip()
answer=1
recur=0
for i in range(len(s)):
    if(i==0):
        if(s[i]=="c"):
            answer*=26
        else:
            answer*=10
    else:
        if(s[i]==s[i-1]):
            recur=1
        else:
            recur=0
        if(s[i]=="c"):
            answer*=(26-recur)
        else:
            answer*=(10-recur)

print(answer)