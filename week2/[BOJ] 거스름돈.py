# 잔돈: 500, 100, 50, 10, 5, 1
# 잔돈 개수가 적게 나오도록 -> 단위가 큰 거스름돈을 우선 사용
# 지불할 돈 입력
# 잔돈 최소 개수 return

import sys
input = sys.stdin.readline

N = int(input()) # 지불할 돈 입력
rest = 1000 - N # 잔돈
result = 0 #출력값

money_arr = [500, 100, 50, 10, 5, 1] # 지불 가능한 잔돈 배열

# 잔돈 배열 안을 돌면서 잔돈 갯수 세보기
# 거스름돈을 나눈 몫을 결과에 더하기
# 거슬러준 만큼 거스름돈에서 빼기
for money in money_arr:
    if rest == 0:
        break
    
    result += rest // money
    rest %= money 
    
print(result)