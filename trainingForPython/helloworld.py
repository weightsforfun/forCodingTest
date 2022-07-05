

from tabnanny import check


def Opr(size,pages):
    SIZE=size
    memory=[]
    faults=0
    for i in range(len(pages)):
        if memory.count(pages[i])==0 and len(memory)<SIZE:
            memory.append(pages[i])
            faults+=1
            print(memory)
        elif memory.count(pages[i])==0 and len(memory)==SIZE:
            checkbox=[]
            for j in range(i,len(pages)):
                if(memory.count(pages[j])>0 and not pages[j] in checkbox):
                    checkbox.append(pages[j])
                if(len(checkbox)==2):
                    memory.clear()
                    
                    for k in range(2):
                        memory.append(checkbox[k])
                    memory.append(pages[i])
                    break
            if(len(checkbox)==1):
                print(1)
                memory.clear()
                memory.append(checkbox[0])
                memory.append(pages[i])
            elif(len(checkbox)==0):
                print(0)
                memory.clear()
                memory.append(pages[i])
            faults+=1
            print(memory)
        elif memory.count(pages[i])>0:
            memory.remove(pages[i])
            memory.append(pages[i]) 
            print("hit")
    return faults
print(Opr(3,[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]))