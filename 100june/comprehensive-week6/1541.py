expression=input()
index=0
sign=1
fixed_expression=[[0,0]]

for i in range(len(expression)):
    if(expression[i]=="-"):
        fixed_expression.append([int(expression[index:i]),sign])
        sign=0
        index=i+1
    elif(expression[i]=="+"):
        fixed_expression.append([int(expression[index:i]),sign])
        sign=1
        index=i+1
fixed_expression.append([int(expression[index:]),sign])
fixed_expression.append([0,0])
answer=0
sum_of_negative=0
is_negative=fixed_expression[1][1]

for i in range(1,len(fixed_expression)-1):
    if(not(fixed_expression[i][1]) or not(is_negative)):
        sum_of_negative+=fixed_expression[i][0]
        if(fixed_expression[i+1][1]==0):
            answer=answer-sum_of_negative
            sum_of_negative=0
            is_negative=1
        else:
            is_negative=0
            continue
    else:
        answer+=fixed_expression[i][0]



print(answer)