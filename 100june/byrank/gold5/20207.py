import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key= lambda x: (x[0],-x[1]))


answer=0
start=arr[0][0]
end=arr[0][1]
blocks=[[arr[0][0],arr[0][1]]]
x=end-start+1
y=len(blocks)
for i in range(1,n):
    next_start=arr[i][0]
    next_end=arr[i][1]
    # print("x:",x,"y:",y,"next_start:",next_start,"nexr_end:",next_end,blocks)
    if(next_start>end+1):
        answer+=(x*y)
        blocks.clear()
        blocks.append([next_start,next_end])
        start=next_start
        end=next_end
        x=next_end-next_start+1
        y=len(blocks)
    else:
        flag=0
        for i in range(len(blocks)):
            if(blocks[i][1]<next_start):
                flag=1
                blocks[i][1]=next_end
                end=max(end,next_end)
                x=end-start+1
                break
        if(not flag):
            blocks.append([next_start,next_end])
            end=max(end,next_end)
            x=end-start+1
            y=len(blocks)
answer+=(x*y)
print(answer)
                
