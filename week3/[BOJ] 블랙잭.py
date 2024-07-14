# 양의 정수
# N장의 카드를 모두 숫자가 보이도록 -> 숫자 M 선택
# 플레이어: N장의 카드 중 3개 고르기
# 3장의 합 < M (최대한 M과 가깝게 만들기)
# 카드 3장의 합 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #N장의 카드, 선택한 숫자 M
n_list = list(map(int, input().split())) # N개의 숫자 리스트
sum = 0 # 카드 3장의 합

# 리스트 중 3개를 골라야 하므로 첫번째 숫자는 n-2 개 중 하나 선택 가능
for i in range(N-2):
    # 두 번째 숫자는 첫 번째 카드를 제외한 n-1 개 중 하나 선택 가능
    for j in range(i+1, N -1):
        # 마지막 숫자는 두 카드를 제외한 n개 중 하나 선택 가능함
        for k in range(j+1, N):
            if (n_list[i] + n_list[j] + n_list[k] <= M):
                # 최댓값 구하기
                sum = max(sum, n_list[i]+n_list[j]+n_list[k])

print(sum)