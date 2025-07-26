def solution(s):
    counts = [0] * 26 #알파벳 개수만큼 빈도수 배열 생성
    
    #문자열의 각 문자에 대한 빈도수를 빈도수 배열에 저장
    for c in s:
        counts[ord(c) - ord('a')] += 1
        
    
    #빈도수 배열을 순회하면서 정렬된 문자열을 생성
    sorted_str = ""
    for i in range(26):
        sorted_str += chr(i + ord('a')) * counts[i]
        
    return sorted_str

#print(solution('hello'))