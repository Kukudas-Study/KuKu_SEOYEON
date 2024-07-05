# 앞뒤만 체육복 빌려주기 가능
# 최대한 많은 학생들이 들을 수 있는 경우
# 전체학생: n / 도난 학생들 번호 배열: lost / 여별 학생들 번호 배열: reserve

def solution(n, lost, reserve):
    new_set = set(lost) & set(reserve) # lost와 reserve 교집합
    # 여벌 가져온 사람이 도난당한 경우를 생각하기 위해서 교집합 구하기

    lost_s = set(lost) - new_set # 체육복을 빌려야 하는 학생들
    reserve_s = set(reserve) - new_set # 여분 가지고 오고 도난 안 당한 학생들(빌려줌 가능)

    for x in sorted(reserve_s):
        if x - 1 in lost_s: # 앞 번호 학생이 빌려야 하는 경우
            lost_s.remove(x - 1)
        elif x + 1 in lost_s: # 뒷 번호 학생이 빌려야 하는 경우
            lost_s.remove(x + 1)
    
    # 빌리지 못한 학생들을 빼주기
    return n - len(lost_s)