amount=int(input())
mans=[]

class man:
    def __init__(self, weight, tall):
        self.weight=weight
        self.tall=tall
        self.rank=1

for i in range(0,amount):
    weight,tall=map(int,input().split())
    mans.append(man(weight,tall))

for i in mans:
    for j in mans:
        if(i.weight<j.weight and i.tall<j.tall):
            i.rank=i.rank+1

for i in mans:
    print(i.rank, end=" ")