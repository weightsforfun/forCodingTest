stairs_nums=int(input())
stairs=[]
for i in range(stairs_nums):
    stair=int(input())
    stairs.append(stair)
stairs.reverse()

max_value=[0]*stairs_nums 

def find_max_value(stair_index,move_length):
    if(stair_index<0):
        return 0
    if(max_value[stair_index]>0):
        return max_value[stair_index]
    if(move_length==1):
        max_value[stair_index]=find_max_value(stair_index-2,2)+stairs[stair_index]
        return max_value[stair_index]
    else:
        max_value[stair_index]= max(find_max_value(stair_index-1,1),find_max_value(stair_index-2,2))+stairs[stair_index]
        return max_value[stair_index]

print(find_max_value(stairs_nums-1,0))

        
