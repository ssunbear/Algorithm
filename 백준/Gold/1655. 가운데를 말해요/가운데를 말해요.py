import sys, heapq
input = sys.stdin.readline

def insertNum(num):
    temp_right = 0
    temp_left = 0
    if len(left_max_heap)==len(right_min_heap):
        heapq.heappush(left_max_heap, [(-1)*num, num])
    else:
        heapq.heappush(right_min_heap, num)

    if right_min_heap:
        if left_max_heap[0][1] > right_min_heap[0]:
            temp_right = heapq.heappop(right_min_heap)
            temp_left = heapq.heappop(left_max_heap)[1]
            heapq.heappush(right_min_heap, temp_left)
            heapq.heappush(left_max_heap, [(-1)*temp_right, temp_right])

N = int(input())
left_max_heap = []
right_min_heap = []

for i in range(N):
    num = int(input())
    insertNum(num)
    print(left_max_heap[0][1])