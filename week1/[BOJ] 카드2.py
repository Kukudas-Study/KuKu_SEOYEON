# popleft()와 append() 반복해서 하나의 원소가 남을때까지

from collections import deque

def find_last_card(N):
    queue = deque(range(1, N + 1))

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

N = int(input())
print(find_last_card(N))