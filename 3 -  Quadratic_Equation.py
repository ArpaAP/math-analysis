from cmath import sqrt

a, b, c = map(int, input('a, b, c = ').split())

D = b**2 - 4 * a * c

alpha = (-b - sqrt(D)) / (2 * a)
beta = (-b + sqrt(D)) / (2 * a)

if D == 0: # 중근을 가지는 경우
    print(f'x={(-b / 2 * a):g} (중근)')
elif D > 0: # 두 실근을 가지는 경우
    print(f'x={alpha.real:g}', '또는', f'x={beta.real:g}')
else: # 두 허근을 가지는 경우
    print(f'x={alpha.real:g}{alpha.imag:+}i', '또는', f'x={beta.real:g}{beta.imag:+}i')


