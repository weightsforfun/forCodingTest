stairs_nums=int(input())
stairs=[0]*301
for i in range(stairs_nums):
    stairs[i]=int(input())


max_value=[0]*301

max_value[0]=stairs[0]
max_value[1]=stairs[0]+stairs[1]
max_value[2]=max(stairs[1]+stairs[2],stairs[0]+stairs[2])

for i in range(3,stairs_nums):
    max_value[i]=max(stairs[i-1]+max_value[i-3],max_value[i-2])+stairs[i]

print(max_value[stairs_nums-1])
    
        
