from collections import deque
def solution(prices):
    answer = []
    que=deque(prices)  # queue 선언
    while(que):
        price=que.popleft() ## pop --> list길이가 점점 짧아지면서 for문 효율 증가
        cnt=0 # cnt 초기화
        for com_price in que : 
            cnt+=1  ## 다음에바로 떨어지더라도 1초 후라는 조건이므로 비교하자마자 증가해도됨
            if price > com_price : # 가격이 떨어지자마자 break 치고 나오면 맞음
                break
        answer.append(cnt) # 증가된거 list에 저장하고 다음 pop으로 이동

    return answer