stack = []

#스택에 데이터 추가
stack.append(1)
stack.append(2)
stack.append(3)

#스택에서 데이터 꺼냄
top_element = stack.pop()
next_element = stack.pop()

#스택 크기
stack_size = len(stack)

print(stack, stack_size, top_element, next_element)