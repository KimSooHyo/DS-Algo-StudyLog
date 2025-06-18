queue = []

#큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

#큐의 맨 앞 데이터 제거
first_item = queue.pop(0) #인수로 0을 넣음 -> 스택과 차이점
print(first_item)

#큐에 데이터 추가
queue.append(4)
queue.append(5)

#큐의 맨 앞 데이터 제거
first_item = queue.pop(0)
print(first_item)