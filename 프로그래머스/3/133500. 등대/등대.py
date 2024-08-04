import sys
sys.setrecursionlimit(100001)
from collections import deque

def dfs(graph, node, visited, LH):
    lighthouse_status = []
    visited[node] = True
    need_turn_on = False
    
    for next_node in graph[node]:
        if not visited[next_node]:
            lighthouse_status.append(dfs(graph, next_node, visited, LH))

    if 1 <= lighthouse_status.count(False):
        LH[node] = True
        return True
        
    return need_turn_on

def solution(n, lighthouse):
    answer = 0
    LH = [False] * (n + 1) 
    visited = [False] * (n + 1)
    graph = [[] * n for _ in range(n + 1)]

    for start, end in lighthouse:
        graph[start].append(end)
        graph[end].append(start)
        
    dfs(graph, lighthouse[0][0], visited, LH)

    count_true = LH.count(True)
    return count_true