#Counter는 리스트를 값으로 주게 되면 해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환
#https://hongcoding.tistory.com/12
from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')