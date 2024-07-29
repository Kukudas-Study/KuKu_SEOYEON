# 자연수 N 주어짐
# 3이면 9까지 자연수를 NxN 표에 채우도록

# 나선형으로 중앙에 1 배치
# 돌아가면서 숫자를 배열에 추가해준다

n = int(input()) # 자연수
m = int(input()) # 위치를 찾고자 하는 자연수 (n^2 보다 작음)
snail = [[0 for _ in range(n)] for _ in range(n)] # 달팽이

# (x, y) 좌표가 정중앙에 위치하도록 계산
x = (n-1)/2
y = (n-1)/2

# 상하좌우
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

direction = 0 # 현재 이동 방향 (초기에는 상)
cnt = 1
rep = 1 # 이동할 횟수

answer_y, answer_x = 0, 0


# 상하좌우로 움직이면서 숫자 지정
while cnt <= n** 2:
    for _ in range(2):
        for _ in range(rep):
            if cnt <= n ** 2:
                snail[y][x] = cnt
                x += dx[direction]
                y += dy[direction]
                cnt += 1

        direction = (direction + 1) % 4
    rep += 1

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=' ')
        if snail[i][j] == m:
            answer_y = i
            answer_x = j

    print()

print(answer_y+1, answer_x+1)