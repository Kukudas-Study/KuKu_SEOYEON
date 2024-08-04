def solution(sizes):
    width = []
    height = []

    # 각 명함의 크기를 순회
    for i in range(len(sizes)):
        # 명함의 가로와 세로 비교
        if(sizes[i][0] > sizes[i][1]):
            # 가로 길이가 더 크면 가로 리스트에 큰 값을, 세로 리스트에 작은 값을 추가
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        else:
            # 세로 길이가 더 크거나 같으면 가로 리스트에 큰 값을, 세로 리스트에 작은 값을 추가
            width.append(sizes[i][1])
            height.append(sizes[i][0])
    
     # 가장 큰 가로 길이와 가장 큰 세로 길이를 곱하여 지갑의 최소 크기 반환
    return max(width) * max(height)