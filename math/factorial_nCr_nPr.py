# factorial_nCr_nPr.py
MOD = 10**9 + 7

def mod_pow(a, b, mod=MOD):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

def factorial(n, mod=MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i-1] * i) % mod
    return fact

def mod_inverse(a, mod=MOD):
    return mod_pow(a, mod - 2, mod)

def nCr(n, r, fact, mod=MOD):
    if r < 0 or r > n:
        return 0
    return fact[n] * mod_inverse(fact[r], mod) % mod * mod_inverse(fact[n-r], mod) % mod

def nPr(n, r, fact, mod=MOD):
    if r < 0 or r > n:
        return 0
    return fact[n] * mod_inverse(fact[n-r], mod) % mod

# ===== 사용 예시 =====
# N = 10
# fact = factorial(N)
# print(nCr(10, 3, fact))
# print(nPr(10, 3, fact))

