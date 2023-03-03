def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    parent=[0]*n
    for i in range(n):
        parent[i]=i
    
    def find(a):
        if(a!=parent[a]):
            parent[a]=find(parent[a])
        return parent[a]
    def union(a,b):
        a=find(a)
        b=find(b)
        if(a<b):
            parent[a]=b
        else:
            parent[b]=a
    for cost in costs:
        a,b,cost=cost
        if(find(a)!=find(b)):
            union(a,b)
            answer+=cost
    return answer