# list 만들어서 처음 값 false
# 2부터 자신의 배수를 지우기
# 리스트값 true로 변경하면 소수만 if문 통과

N, K = map(int, input().split())
cnt = 0
n_list = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if n_list[j] != False:
            n_list[j] = False
            cnt += 1
            if cnt == K:
                print(j)