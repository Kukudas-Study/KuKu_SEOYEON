import sys
input = sys.stdin.readline

# 같은 행의 중복된 숫자 체크
def check_row(row, n):
    for i in range(9):
        if sudoku[n][i] == row:
            return False
    return True

# 같은 열의 중복된 숫자 체크
def check_col(col, n):
    for i in range(9):
        if sudoku[i][n] == col:
            return False
    return True

# 같은 칸의 중복된 숫자 체크
def check_rect(row, col, n):
    # 각 칸의 시작 인덱스 구하기
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == n:
                return False
    return True

def dfs(n):
    if n == len(empty):
    	# 답을 찾으면 프로그램 종료
        for i in range(9):
            print(*sudoku[i])
        exit()

    # 빈자리에 1~9 넣어보고 가능하면 재귀함수 호출
    row = empty[n][0]
    col = empty[n][1]
    for i in range(1, 10):
        if check_row(i, row) and check_col(i, col) and check_rect(row, col, i):
            sudoku[row][col] = i # 숫자 넣기
            dfs(n+1)
            sudoku[row][col] = 0 # 종료하면 다시 초기화

sudoku = [list(map(int, input().split()))for _ in range(9)]
empty = [] # 빈자리

# 스도쿠 판에 숫자 채우고 빈 곳은 따로 empty에 추가
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append([i, j])

dfs(0)