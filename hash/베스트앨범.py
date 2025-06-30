def solution(genres, plays):
    answer = []
    
    genres_dict = {}
    plays_dict = {}
    
    # 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
    for i in range(len(plays)):
        g = genres[i]    
        p = plays[i]
        if g not in genres_dict:
            genres_dict[g] = []
            plays_dict[g] = 0
        
        genres_dict[g].append((i, p))
        plays_dict[g] += p
    
    # 총 재생 횟수가 많은 장르 순으로 정렬
    sorted_genres = sorted(plays_dict.items(), key = lambda x : x[1], reverse=True)
    
    #각 장르 내에서 노래를 재생 횟수 순으로 정렬해 최대 2곡 선택
    for genre, _ in sorted_genres:
        #재생 횟수가 같다면 고유 번호가 낮은 노래를 먼저 수록해야하기 때문에 -x[1]로 이를 표현
        sorted_songs = sorted(genres_dict[genre], key = lambda x : (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
        
    return answer