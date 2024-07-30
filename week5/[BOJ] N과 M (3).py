import sys
input = sys.stdin.readline

# 숫자를 cnt만큼 선택한 상태에서 arr[cnt]를 고르는 함수
def dfs(cnt):
    # 종료 조건
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr[cnt] = i
        dfs(cnt + 1)

n, m = map(int, input().split())
arr = [0 for _ in range(m)] # 고른 m개의 숫자가 담기는 리스트
dfs(0)