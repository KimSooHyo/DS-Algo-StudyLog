import functools

def compare(a,b):
    #각 수를 문자열로 바꾼 뒤, 조합하여 비교하여 더 큰 수 반환
    t1 = str(a) + str(b)
    t2 = str(b) + str(a)
    #t1 > t2이면 1, t1 < t2이면 -1, 같으면 0 반환
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    #reverse = True를 이용해 내림차순 정렬
    sorted_nums = sorted(
        numbers, key = functools.cmp_to_key(lambda a, b: compare(a,b)), reverse=True
    )
    #각 정렬된 수를 문자열로 이어붙인 뒤, int로 변환한 값을 문자열로 다시 변환하여 반환
    answer = "".join(str(x) for x in sorted_nums)
    return "0" if int(answer) == 0 else answer