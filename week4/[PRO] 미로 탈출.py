# 벽 뺴고 전부 지나갈 수 있음
# 출발 -> 레버, 레버 -> 출구 bfs 수행
# 만약 path가 존재하지 않으면 return -1


from collections import deque

def bfs(start, end, maps):
    # 탐색 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]

    # 세로
    n = len(maps)
    # 가로
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    flag = False

    # 초기값 설정하기
    for i in range(n):
        for j in range(m):
            # 출발하는 지점이라면 시작점 좌표 기록
            if maps[i][j] == start:
                q.append((i, j, 0))
                visited[i][j] = True
                # 시작점은 한 개만 존재하기 때문에 찾으면 바로 break
                flag = True; break
        if flag: break

    while q:
        y, x, cost = q.popleft()

        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # maps 범위 내라면 지나가기 가능
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    q.append((ny, nx, cost + 1))
                    visited[ny][nx] = True
    # 탈출 하지 못한 경우
    return -1

def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)

    # 둘다 -1 아니라면 탈출 가능
    if path1 != -1 and path2 != -1:
        return path1 + path2
    
    return -1