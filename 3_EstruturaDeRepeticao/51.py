'''
51 - Faça um programa que mostre os n termos da Série a seguir:

Imprima no final a soma da série.
'''

n = int(input('Digite o número: '))
s = 0
d = 1
print('S=',end=' ')
for i in range(1, n + 1):
    if i == n:
        print(f'{i}/{d}',end=' ')
    else:
        print(f'{i}/{d}',end=' + ')
    s += i / d
    d += 2
print('\nSoma da sequência: %.2f' % s)
    
