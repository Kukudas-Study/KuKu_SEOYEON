def solution(tickets):
    answer = []
    visited = [False] * len(tickets) # 티켓 사용 여부 기록
    
    def dfs(airport, path):
        # 모든 티켓을 사용한 경우
        if len(path) == len(tickets) + 1:
            answer.append(path) # 결과를 리스트에 추가
            return
        
        # 티켓을 순회하며 탐색
        for idx, ticket in enumerate(tickets):
            # 현재 공항이 티켓의 출발지와 같고, 해당 티켓을 사용하지 않은 경우
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True # 티켓 사용
                dfs(ticket[1], path+[ticket[1]]) # 도착지로 이동하여 경로 추가
                visited[idx] = False

    # 시작이 "ICN" 
    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]