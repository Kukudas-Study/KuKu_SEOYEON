A, B, C, M = map(int, input().split())

fatigue = 0
work = 0

# 하루가 24시간이니까 range도 24시간
for _ in range(24):
    if M < A:
        break

    # 일을 할 수 있는 경우
    if fatigue + A <= M:
        fatigue += A
        work += B
    else: # 일을 할 수 없는 경우
        fatigue -= C # 피로도가 c만큼 감소

        if fatigue < 0: # 쉬어서 피로도가 음수이면 피로도는 0
            fatigue = 0

print(work)