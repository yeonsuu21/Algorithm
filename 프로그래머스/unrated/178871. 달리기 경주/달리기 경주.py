def solution(players, callings):
    #선수이름 부르면 순위가 바로 앞으로 바뀌는것
    #딕셔너리 이용한다 : 왜? - 용량 때문에
    players_dict = dict()
    for idx, values in enumerate(players):
        players_dict[values] = idx
    
    for call in callings:
        rank = players_dict[call] # 현재 랭킹
        
        # 딕셔너리 위치 변경
        players_dict[call] -=1
        players_dict[players[rank-1]] +=1
        
        # 배열 위치 변경
        players[rank-1], players[rank] = call, players[rank-1]
                
    answer = players
    return answer