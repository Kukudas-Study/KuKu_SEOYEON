from collections import deque

# 제한사항에 500
visited = [[0 for _ in range(500)] for _ in range(500)]

def bfs(y, x, n, m, land, answer_list):
    q = deque()
    q.append([y, x])
    # 면적 크기
    count = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    visited[y][x] = 1
    visited_x = [x] # 면적과 만나는 열 번호

    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if land[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    if nx not in visited_x:
                        visited_x.append(nx)

                    q.append([ny, nx])
                    count += 1

    # 면적과 만나는 열 번호에 면적 크기를 더하기
    for connected_x in visited_x:
        answer_list[connected_x] += count

def solution(land):
    n = len(land)
    m = len(land[0])
    answer_list = [0 for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, n, m, land, answer_list)

    answer = max(answer_list)
    return answer