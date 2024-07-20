import sys
sys.setrecursionlimit(10000)
# 런타임 에러를 방지하기 위함

# 상하좌우 위치에 대해 재귀함수를 호출하는 dfs 함수 이요
# 특정 위치에 배추가 있을 떄(값이 1일 떄)만 작동
# 탐색한 경우 값을 0으로 변경

T = int(input())
resultArr = [0 for i in range(T)] # 출력을 위한 리스트

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x -1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for t in range(T):
    m, n, k = map(int, sys.stdin.readline().split()) # 가로, 세로 길이 / 배추 개수
    graph = [[0 for x in range(m)] for y in range(n)]

    # 배추 심기
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0

    # 결과가 True이면 결과 +1
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                resultArr[t] += 1

for i in range(T):
    print(resultArr[i])