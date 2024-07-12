from collections import deque

def solution(board):
    n,m=len(board), len(board[0])
    queue=deque()
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    visited=[[0 for _ in range(m) ] for _ in range(n)]
    answer=0
    
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                queue.append([i,j,0])
                
    while queue:
        x, y, answer= queue.popleft()
        for dx, dy in directions:
            mx,my=x+dx,y+dy
            while 0<=mx<n and 0<=my<m and board[mx][my] !='D':
                mx,my = mx+dx,my+dy
            mx,my=mx-dx,my-dy
            
            if board[mx][my]=='G':
                return answer+1
            
            if not visited[mx][my]:
                visited[mx][my]=1
                queue.append([mx,my,answer+1])
                
    return -1
