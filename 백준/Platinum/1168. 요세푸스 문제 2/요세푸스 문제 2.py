from sys import stdin

input = stdin.readline

#세그먼트 트리 생성
def init(tree, node, start, end):
    if start==end:
        tree[node] = 1
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(tree, node*2,start, mid) + init(tree, node*2+1, mid+1, end)
    return tree[node]

#dellete를 제거
def update(tree, node, start, end, dellete):
    tree[node] -=1
    if start==end:
        return 0

    else:
        mid = (start+end)//2
        if dellete<=mid:
            return update(tree, node*2, start, mid,dellete)
        else:
            return update(tree, node*2+1, mid+1, end, dellete)

#order번째 수 반환
def query(tree, node, start, end, order):
    if start==end:
        return start
    
    mid = (start + end)//2

    if order <= tree[node*2]:
        return query(tree, node*2, start, mid, order)
    else:
        return query(tree, node*2+1, mid+1, end, order-tree[node*2]) #tree[node*2]다음으로 몇번째 수인지 찾기 위해서 order에서 tree[node*2]를 빼준다.



n, k = map(int,input().split())
tree = [0]*3000000

init(tree,1, 1, n) 
index = 1

array = list()

for i in range(n):
    
    size = n-i
    index += k-1

    if index%size == 0: #index가 size를 넘었을때 mod연산을 해야하는데 0이 되면 안되기 때문이다.
        index = size
    elif index>size: #index가 size를 넘지 않도록 mod연산
        index %= size

    num = query(tree, 1, 1, n, index) #index번째 수를 저장

    update(tree, 1, 1, n, num) #index번째 수 제거
    array.append(str(num))

print("<",", ".join(array),">",sep='')