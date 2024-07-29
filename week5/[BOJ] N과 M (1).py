import sys
input = sys.stdin.readline

# def는 재귀함수로 반복되므로 출력 조건을 먼저 줘야 한다
def dfs():
    # 함수 출력 조건 (리스트 s 안에 m개의 요쇼가 쌓이면 출력)
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    # 이미 방문한 곳은 방문하지 않기
    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            dfs()
            array.pop()


n, m = map(int, input().split())
array = []

dfs()