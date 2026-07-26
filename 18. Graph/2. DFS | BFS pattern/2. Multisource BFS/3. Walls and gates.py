from os import *
from sys import *
from collections import *
from math import *
from collections import deque

def wallsAndGates(a, n, m): 
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                q.append((i, j))
        
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 2147483647:
                a[nr][nc] = a[r][c] + 1
                q.append((nr, nc))
    return a
    
