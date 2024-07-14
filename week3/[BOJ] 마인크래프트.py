# 3차원
# 세로 N, 가로 M크기의 집 (0,0)부터 시작
# 땅 고르기 작업
# 1. (i,j) 가장 위에 있는 블록 제거하여 인벤토리에 넣기 (2초)
# 2. 인벤토리에서 좌표 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓기 (1초)

# 작업에 걸리는 최소 시간, 땅의 높이 출력
# 시작할때 인벤토리: B개의 블록 존재


import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.extend(map(int, sys.stdin.readline().split()))

height = 0
time = [0 for i in range(257)] # 땅높이가 k일때의 소요시간 저장 (최대가 256이므로 범위 제한)

# 각 블록의 초과분 찾기 (최대 256층이므로 그 안에서)
for g in range(257):
    block = B # 인벤토리에 남은 블록 수
    for i in ground:
        if i <= g: # i == g이면 g-i=0
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    if block >= 0 and time[g] <= time[height]: 
        # 오름차순으로 순회/ 답이 여러 개 있을 때 그중에서 땅의 높이가 가장 높은 것을 저장하게 됨
        height = g # 최소 소요 시간인 땅높이 저장

print(time[height], height)