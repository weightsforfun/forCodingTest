def dfs(users,depth,cart,emoticons,answer):
    discounts=[10,20,30,40]
    if(depth==len(emoticons)):
        count=0
        price=0
        for i in range(len(cart)):
            if(cart[i]>=users[i][1]):
                count+=1
            else:
                price+=cart[i]

        if(answer[0]<count or(answer[0]<=count and answer[1]<=price)):
            answer[0]=count
            answer[1]=price
        return 
    for discount in discounts:

        for i in range(len(users)):
            if(users[i][0]<=discount):
                cart[i]+=(emoticons[depth]*(100-discount)//100)

        dfs(users,depth+1,cart,emoticons,answer)

        for i in range(len(users)):
            if(users[i][0]<=discount):
                cart[i]-=(emoticons[depth]*(100-discount)//100)

def solution(users, emoticons):
    answer = [0,0]
    cart=[0]*len(users)
    dfs(users,0,cart,emoticons,answer)

    return answer