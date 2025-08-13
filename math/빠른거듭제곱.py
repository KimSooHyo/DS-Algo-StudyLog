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

# ===== 사용 예시 =====
# print(mod_pow(2, 10))  # 2^10 mod MOD
