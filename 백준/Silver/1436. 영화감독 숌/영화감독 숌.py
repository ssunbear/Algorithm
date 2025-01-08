n=int(input())
list_666=[]

for x in range(666,1000000001):
    if '666' in str(x):
        list_666.append(x)
    if len(list_666)==n:
        break

print(list_666[n-1])   