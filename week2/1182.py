from itertools import combinations
 
count,target=map(int,input().split(" "))
numbers=list(map(int,input().split(" ")))
answers=0



		

for i in range(1,count+1):
	comb=combinations(numbers,i)
	for j in list(comb):
		if(sum(j)==target):
			answers=answers+1

print(answers)