test_cases=int(input())
cases_arr=[]
length_of_triangle=[0]*101
for i in range(test_cases):
    cases_arr.append(int(input()))

length_of_triangle[1]=1
length_of_triangle[2]=1
length_of_triangle[3]=1

def guess_length(n):
    if(length_of_triangle[n]!=0):
        return length_of_triangle[n]
    else:
        length_of_triangle[n]=guess_length(n-2)+guess_length(n-3)
        return length_of_triangle[n]
for i in cases_arr:
    print(guess_length(i))