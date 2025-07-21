"""
9x9 스도쿠 보드를 다 채워 완성된 스도쿠 보드를 반환
"""

def is_valid(num, row, col, board): #유망 함수
    #현재 위치에 num이 들어갈 수 있는지 검사
    return not (in_row(num, row, board) or in_col(num, col, board) or in_box(num, row, col, board))

def in_row(num, row, board):
    #해당 행에 num이 있는지 확인
    return num in board[row]

def in_col(num, col, board):
    #해당 열에 num이 있는지 확인
    return num in (board[i][col] for i in range(9))

def in_box(num, row, col, board):
    #현재 위치의 3x3 박스에 num이 있는지 확인
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return True
    return False

def find_empty_position(board):
    #스도쿠 보드에서 비어있는 위치 반환
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def find_solution(board):
    #비어있는 위치에 가능한 숫자를 넣어가며 스도쿠 해결
    empty_pos = find_empty_position(board)
    #빈칸이 없으면 스도쿠가 해결된 것으로 간주
    if not empty_pos:
        return True
    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(num, row, col, board):
            board[row][col] = num
            if find_solution(board): #다음 빈칸을 재귀 탐색
                return True
        board[row][col] = 0 #가능한 숫자가 없으면 원래의 0으로 되돌림
    return False

def solution(board):
    find_solution(board)
    return board