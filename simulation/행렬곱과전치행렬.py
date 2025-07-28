def multiply_matrics(matrix1, matrix2):
    #결과 행렬을 0으로 초기화
    result = [[0,0,0],[0,0,0],[0,0,0]]
    #행렬 곱셈을 수정
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result

def transpose_matrix(matrix):
    #결과 행렬 0으로 초기화
    result = [[0,0,0],[0,0,0],[0,0,0]]
    
    #전치 행렬을 계산
    for i in range(3):
        for j in range(3):
            result[j][i] = matrix[i][j]
            
    return matrix

def solution(matrix1, matrix2):
    #주어진 두 행렬 곱하기
    multiplied = multiply_matrics(matrix1, matrix2)
    #곱셈 결과의 전치행렬 계산
    transposed = transpose_matrix(multiplied)
    return transposed