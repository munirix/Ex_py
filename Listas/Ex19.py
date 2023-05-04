
print('Qual o melhor Sistema Operacional para uso em servidores?')
print('''1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro''')

opcoes = ['Windows', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
sistemas = [0] * 6
while True:
    while True:
        opcao = int(input('Digite a opção: '))
        if opcao > 6 or opcao < 0:
            print('Opção inválida.')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1


print('\nSistema Operacional\tVotos\t\t%')
print('----------------------------------------')
cont = 0
melhor = 0
melhorSis = ''
perc = 0
for s in sistemas:
    print('%s\t\t\t%d\t\t%.2f%%' % (opcoes[cont], s,(s * 100) / sum(sistemas) ))
    if s > melhor:
        melhor = s
        melhorSis = opcoes[cont]
        perc = (s * 100) / sum(sistemas)
    cont += 1

print('----------------------------------------')
print('Total de votos = %d' % sum(sistemas))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f %% dos votos.\n' % (melhorSis, melhor, perc))