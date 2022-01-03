quantity=int(input())
glasses=[]
max_drinks=[0]*quantity
for i in range(quantity):
    glasses.append(int(input()))
max_drinks[0]=glasses[0]
if(quantity>=2):
    max_drinks[1]=glasses[1]+glasses[0]
if(quantity>=3):
    max_drinks[2]=max(max(glasses[0],glasses[1])+glasses[2],max_drinks[1])
for i in range(3,quantity):
    max_drinks[i]=max(max(glasses[i-1]+max_drinks[i-3],max_drinks[i-2])+glasses[i],max_drinks[i-1])
print(max_drinks[quantity-1])
