n=int(input())
answers=[-1]*1000001

answers[0]=1
answers[1]=2
answers[2]=3


for i in range(3,n+1):
    answers[i]=(answers[i-1]+answers[i-2])%15746

print(answers[n-1])

