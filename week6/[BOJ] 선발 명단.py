import sys
input = sys.stdin.readline

T = int(input())

def backtracking(count, sum):
    global result

    # 최대 점수 계산
    if count == 11:
        result = max(result, sum)
        return
    
    for i in range(11):
        # 이미 포지션이 존재하거나 해당 포지션이 맞지 않은 경우
        if members[i] or not powers[count][i]:
            continue

        members[i] = 1 # 방문 가능 상태
        backtracking(count+1, sum+powers[count][i]) # 백트래킹 반복
        members[i] = 0

for _ in range(T):
    powers = [list(map(int, input().split())) for _ in range(11)]
    members = [0 for _ in range(11)] # members
    result = 0

    backtracking(0, 0)
    print(result)