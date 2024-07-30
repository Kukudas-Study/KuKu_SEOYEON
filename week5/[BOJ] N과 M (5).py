n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort() # 낮은 순으로 정렬
visited = [False] * n # 방문 여부
arr = []

def dfs():
    # 탈출 조건
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(n):
        if not visited[i]:
            arr.append(data[i])
            visited[i] = True
            dfs()
            visited[i] = False
            arr.pop()

dfs()