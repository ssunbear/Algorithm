import heapq

k,n=map(int,input().split())
prime=list(map(int,input().split()))
heap=[]
answer=0
for i in prime:
    heap.append(i)

for i in range(n):
    answer=heapq.heappop(heap)
    for x in prime:
        heapq.heappush(heap, x*answer)
        if answer%x==0:
            break

print(answer)