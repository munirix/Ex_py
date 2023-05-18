'''
38. Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
ao dobro do percentual do ano
anterior. Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o
programa permitindo que o usuário digite o salário inicial do funcionário.
'''

salario = 1000
aumento = 1.5
ano = 1996
while True:
    for i in range(ano, 1999):
        print('Salário no ano %d = %.2f, aumento de %.2f' % (i, salario, aumento))
        salario += ((salario * aumento) / 100)
        aumento *= 2
    
    print('\nSalário atual: %.2f' % salario)
    print('\n-------------\n')
    proc=int(input('\nDeseja inserir um novo salario inicial?\nSe sim, digite 1\nSe não, digite 0\n'))
    if proc == 1:
        salario=0
        aumento = 1.5
        salario=int(input('\nInsira o salario inicial: '))
    else:
        break
