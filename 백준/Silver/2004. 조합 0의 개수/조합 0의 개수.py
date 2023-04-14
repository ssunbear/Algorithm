#팩토리얼로 푸면 메모리제한
#10의 배수를 잘 활용 (2개수, 5개수중 적은것이 10의 개수)
import sys
def countnum(N, num):
    count=0
    div=num
    while(N>=div):
        count += (N//div)
        div*=num
    return count

n,m=map(int, sys.stdin.readline().split())
print(min(countnum(n,5)-countnum(m,5)-countnum(n-m,5),countnum(n,2)-countnum(m,2)-countnum(n-m,2)))