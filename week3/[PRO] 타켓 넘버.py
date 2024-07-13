def solution(numbers, target):
    answer = 0
    leaves = [0]

    for num in numbers:
        temp = []
        for parent in leaves:
            temp.append(parent+num)
            temp.append(parent - num)
            # numbers의 숫자를 더하거나 뺀 경우를 수평적으로추가
        leaves = temp
    
    # leaves에 모든 계산 결과가 존재하므로 target값과 비교해서 aswer에 +1
    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer