# 에라토스테네스의 체
import numpy as np

# 범위 지정
N = 1000

# 체
a = [False, False] + [True]*(N-1)

# 걸러진 소수들
primes = []

for i in range(2, N+1):
    # 걸리지지 않은 수에 대하여
    if a[i]:
        primes.append(i)
        # 합성수일 경우 걸러짐
        for j in range(2*i, N+1, i):
            a[j] = False

print(np.array_str(np.array(primes), precision=10))



