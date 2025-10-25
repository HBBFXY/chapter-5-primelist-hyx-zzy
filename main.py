import math

def PrimeList(N):
    primes = []
    for x in range(2, N):
        is_prime = True
        # 检查2到根号x的所有数
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(x))
    # 将列表转为空格分隔的字符串
    return ' '.join(primes)
