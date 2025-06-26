import random

true_value = random.randint(1, 100)
print("숫자를 맞춰보세요")
answer = 101
while true_value != answer:
    answer = int(input())
    if answer > true_value:
        print("숫자가 너무 큽니다")
    elif answer < true_value:
        print("숫자가 너무 작습니다")

print(f"정답입니다! 정답은 {true_value}입니다")
    
    