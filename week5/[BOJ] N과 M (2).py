# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

# 조합 이용해보기
from itertools import combinations

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]

for seq in combinations(numList, M):
    print(*seq)