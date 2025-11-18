import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    rows = len(maps)
    cols = len(maps[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    vis = [[False for _ in range(cols)] for _ in range(rows)]
    
    def bfs(r,c) :
        vis[r][c] = True
        area = 0
        for i in range(4) :
            r1,c1 = r + dr[i], c + dc[i]
            if 0 <= r1 < rows and 0 <= c1 < cols and maps[r1][c1] != 'X' and not vis[r1][c1] :
                area += bfs(r1,c1) 
        return int(maps[r][c]) + area

    for i in range(rows) :
        for j in range(cols) :
            if vis[i][j] == False and maps[i][j] != 'X':
                answer.append(bfs(i,j))

    if answer :
        answer.sort()
    else :
        answer = [-1]
    return sorted(answer)