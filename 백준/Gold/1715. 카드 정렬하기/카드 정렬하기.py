import heapq

n = int(input())
card = []
for i in range(n):
    card.append(int(input()))
heapq.heapify(card)

answer = 0
while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    result = first + second
    answer += result
    heapq.heappush(card, result)

print(answer)
