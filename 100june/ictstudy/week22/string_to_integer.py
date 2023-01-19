s=input()
s=s.lstrip()
string=list(s)
negative=0
only_digit=0
answer=[]
while(True):
    if(only_digit):
        if(len(string)==0):
            break
        else:
            if(string[0]==' ' or string[0]=='-' or string[0]=='+'):
                break
            answer.append(string.pop(0))    
    else:
        if(string[0]=='-'):
            negative=1
            only_digit=1
            string.pop(0)
        elif(string[0]=='+'):
            only_digit=1
            string.pop(0)
        elif(string[0]==' '):
            break
        else:
            answer.append(string.pop(0))
            only_digit=1
if(negative):
    print(int('-'+''.join(answer)))
else:
    print(int(''.join(answer)))


