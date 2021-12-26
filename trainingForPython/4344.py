test_case=input()
results=[]
for i in range(0,int(test_case)):
    student_num_arr=list(map(int,input().split()))
    student_num=student_num_arr[0]
    average=sum(student_num_arr[1:])/student_num
    good_student=0
    for score in student_num_arr[1:]:
        if(score>average):
            good_student=good_student+1
    fixed_result=round((good_student/student_num)*100,3)
    results.append(str('{:.3f}'.format(fixed_result))+"%")
    
    
for result in results:
    print(result)