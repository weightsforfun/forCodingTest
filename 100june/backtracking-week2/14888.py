n=int(input())
numbers=list(map(int,input().split(" ")))
symbols=list(map(int,input().split(" ")))
answers=[]

def calculate(last_num,symbols,index):
	if(n==index):
		answers.append(last_num)
		return ;
	else:
		for i in range(0,4):
			if(symbols[i]!=0):
				symbols[i]=symbols[i]-1
				if(i==0):
					calculate(last_num+numbers[index],symbols,index+1)
					symbols[i]=symbols[i]+1
				elif(i==1):
					calculate(last_num-numbers[index],symbols,index+1)
					symbols[i]=symbols[i]+1
				elif(i==2):
					calculate(last_num*numbers[index],symbols,index+1)
					symbols[i]=symbols[i]+1
				elif(i==3):
					last_num_fixed= last_num>0 and last_num//numbers[index] or (abs(last_num)//numbers[index])*-1
					calculate(last_num_fixed,symbols,index+1)
					symbols[i]=symbols[i]+1

calculate(numbers[0],symbols,1)
print(max(answers),min(answers))