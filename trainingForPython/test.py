children=[1,2,3,4,5,6]
def layback(start,end):
    temp=children[end]
    for i in range(end,start,-1):
        children[i]=children[i-1]
    children[start]=temp
layback(0,5)
print(children)