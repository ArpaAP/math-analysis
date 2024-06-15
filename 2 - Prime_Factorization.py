from time import time
from math import trunc, sqrt

N = int(input('정수 입력: '))

start = time()

ls = []

while N > 1:
    for i in range(2, trunc(sqrt(N+1))):
        # i로 나누어 떨어지는 경우
        if N % i == 0:
            # N을 자기 자신을 i로 나눈 몫으로 갱신
            N //= i
            ls.append(i)

end = time()

print('소인수분해 결과:', '*'.join(map(str, sorted(ls))), end - start, 's')

