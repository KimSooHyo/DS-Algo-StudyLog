#2차원 배열을 90도 회전시키는 함수
def rotate_90(arr):
    n = len(arr)
    rotate_arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotate_arr[j][n-i-1] = arr[i][j]
            
    return rotate_arr

#배열을 n번 90도 회전시키는 함수
def solution(arr, rotations):
    rotate_arr = arr.copy()
    for _ in range(rotations):
        rotate_arr = rotate_90(rotate_arr)
        
    return rotate_arr