from collections import deque



arr=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]


def Opr(size,page_and_refbit):
    SIZE=size
    memory=deque()
    faults=0
    
    for i in range(len(page_and_refbit)):
        flag=0
        is_there_value=0
        index=-1
        for j in memory:
            if(page_and_refbit[i] == j[0]):
                is_there_value=1
            index+=1
        if not is_there_value and len(memory)<SIZE:
            memory.append([page_and_refbit[i],-1])
            faults+=1
            print(memory)
        elif not is_there_value and len(memory)==SIZE:
            for j in range(3):
                if(memory[j][1]==-2):
                    memory.popleft()
                    flag=1
                    break
                else:
                    memory[j][1]=-2
                    memory.append(memory.popleft())
            if(not flag):
                memory.popleft()
            memory.append([page_and_refbit[i],-1])
            faults+=1
            print(memory)
        elif is_there_value:
            memory[index][1]=-1
                
            print("hit")
    return faults
print(Opr(3,arr))