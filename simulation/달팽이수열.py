def solution(n):
    #n크기의 2차원 배열 생성
    snail_array = [[0] * n for _ in range(n)]
    num = 1 #달팽이 수열 시작 숫자
    #행과 열의 시작과 끝 인덱스 설정
    start_row, end_row = 0, n-1
    start_col, end_col = 0, n-1
    
    while start_row <= end_row and start_col <= end_col:
        #첫번째 행 채우기
        for i in range(start_col, end_col+1):
            snail_array[start_row][i] = num
            num += 1
        start_row += 1
        
        #마지막 열 채우기
        for i in range(start_row, end_row + 1):
            snail_array[i][end_col] = num
            num += 1
        end_col -= 1
        
        #마지막 행 채우기
        if start_row <= end_row:
            for i in range(end_col, start_col-1, -1):
                snail_array[end_col][i] = num
                num += 1
            end_row -= 1
        
        #첫번째 열 채우기
        if start_col <= end_col:
            for i in range(end_row, start_row-1, -1):
                snail_array[i][start_row] = num
                num += 1
            start_col += 1
            
    return snail_array