# 에라토스테네스의 체
# n 이하의 모든 소수를 구하는 방법

def sieve(n):
    # 0과 1은 소수가 아니므로 False, 2~n까지 True로 초기화
    is_prime = [False, False] + [True] * (n - 1)
    
    # i가 소수일 경우, i*i 이상 n 이하의 배수를 False 처리
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
                
    # 소수 리스트 반환
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes

# 사용 예시
n = 50
prime_list = sieve(n)
print(f"{n} 이하의 소수:", prime_list)
