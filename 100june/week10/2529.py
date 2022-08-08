import  sys

arr=[0,1,2,3,4,5,6,7,8,9]
used=[0]*10
answers=[]
n=int(sys.stdin.readline())
symbol=list(sys.stdin.readline().split())

def comparison(i,j,k):
    if(k==">"):
        return i>j
    else:
        return i<j

def check_node(index,answer):
    if(index==n):  #깊은 복사를 해야 전역 리스트인 answers에 들어갔다 그냥 append(answer)하면 안들어감
        answers.append(answer)   # 최종 재귀까지 오면 answers에 넣어준다
    else:
        if(answer==""):   # 처음에만 비교할 숫자가 없으므로 값을 넣어준다
            for i in range(0,10):
                used[i]=1
                check_node(0,answer+str(i))
                used[i]=0
        else:    # 그이후로 안사용한 숫자를 넣어서 부등호에따라 일치하면 다음재귀로 아니면 넘어간다
            for i in range(0,10):
                if(used[i]==0):
                    if(comparison(int(answer[-1]),i,symbol[index])):
                        used[i]=1
                        check_node(index+1,answer+str(i))
                        used[i]=0
                    
                        
            


check_node(0,"")
for i in answers[-1]:
    print(i,end="")
print()
for i in answers[0]:
    print(i,end="")




