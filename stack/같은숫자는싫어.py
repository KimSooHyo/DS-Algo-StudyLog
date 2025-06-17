def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        elif answer[-1] == a:
            continue
        else:
            answer.append(a)
    return answer