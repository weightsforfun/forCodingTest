import re

sentence=input()
count=0
croatias=["c=","c-","dz=","d-","lj","nj","s=","z="]
for croatia in croatias:
    if(sentence.find(croatia)!=-1):
        count =count + len(re.findall(croatia,sentence))
        sentence=sentence.replace(croatia,' ')
        
sentence=sentence.replace(' ','')
count=count+len(sentence)
print(count)
        