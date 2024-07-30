def dfs():
    check = 0
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        if check != num[i] and visited[i] == 0:
            arr.append(num[i])
            visited[i] = 1
            check = num[i]
            dfs()
            arr.pop()
            visited[i] = 0


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * n
arr = []
dfs()