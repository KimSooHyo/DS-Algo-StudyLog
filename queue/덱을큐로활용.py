"""
덱 : Double Ended Queue
- 양 끝에서 삽입이나 삭제할 수 있는 큐
    -> 큐를 구현할 때는 덱을 사용하는 것이 좋음
- 리스트의 pop(0)은 시간복잡도가 O(n) 
- 덱의 popleft()는 시간 복잡도가 O(1)
"""

from collections import deque

queue = deque()

#큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

#큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(first_item)

#큐에 데이터 추가
queue.append(4)
queue.append(5)

#큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(first_item)