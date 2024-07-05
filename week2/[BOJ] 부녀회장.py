# a층의 b호에 살려면 a-1층의 1호~b호가지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# k층 n호에는 몇 명이 살고 있는지 출력
# 0층 -> i호에는 i명이 산다

# 예제 1
# test case = 2
# 1) k = 1, n = 3 => 1층의 3호 
# 2) k = 2, n = 3 => 2층의 3호

# 1층의 3호: 0층의 1호~3호까지 사람들의 수 합
# 0층 1호:1 / 2층:2 / 3층:3 => 합 6
# 2층의 3호: 1층의 1호~3호까지 사람들의 수 합
# 1층 1호:1 / 2호:3 / 3층:6 => 합 10


# 0층 사람들은 정해져 있으므로 배열로 지정
# 아래층의 1~n호 합 구하기 반복 => 배열에 추가
# 배열에서 k층 n호 찾아서 출력

T = int(input()) # test case

for i in range(T): # test case만큼 반복
    k = int(input())
    n = int(input())

    people = [i for i in range (1, n + 1)] # 0층부터 1호~n호 사람 수 담기

    for j in range(k):
        for k in range(1, n):
            people[k] += people[k -1] # 아래층 1~n호 값 더하기

    print(people[-1])