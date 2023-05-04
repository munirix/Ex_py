n=int(input("Digite o número do jogador (0=fim): "))
if n!=0:
    votos=23*[0.0]
    total=0
    while n!=0:
        if n<0 or n>23:
            print("Informe um valor entre 1 e 23 ou 0 para sair")
        else:
            votos[n-1]+=1   #adiciona 1 a quantidade de votos do jogador especifico
            total+=1        #adiciona 1 ao total de votos
        n=int(input("Digite o número do jogador (0=fim): "))
    print("Resultado da votação: \n")
    print(f'''Foram computados {total} votos.\n''' )
    print("Jogador\t/\tVotos\t/\tPorcentagem")

    i=0
    j=0
    melhor = 0          #guarda valor numero do melhor jogador
    aux =0              #guarda valor da variavel melhor
    melhores=23*[0]     #guarda valor do numero dos melhores jogadores, caso haja mais de um com os mesmos votos
    melhorPorcentagem=(votos[0]/total)*100  #porcentagem de votos do melhor jogador, inicia com a porcentagem do primeiro

    #varre todos os votos
    while i<23:
        if votos[i]>0:
            porcentagemAtual=(votos[i]/total)*100   #porcentagem de votos do jogador atual
            print('''%d\t/\t%d\t/\t%.1f''' %(i+1, votos[i], porcentagemAtual))
            #caso a porcentagem do jogador atual seja maior do que a antiga maior porcentagem
            if porcentagemAtual> melhorPorcentagem: 
                melhor = i
                aux = melhor
                melhorPorcentagem=porcentagemAtual

                #limpa variavel melhores, para caso ela tenha obtido algum valor
                melhores=23*[0]
                j=0
            
            #caso a porcentagem do jogador atual seja igual a antiga maior porcentagem
            elif porcentagemAtual==melhorPorcentagem:
                melhores[j]+=i+1
                j+=1
                melhor=0
        i+=1
    if melhor!=0:
        print("\nO melhor jogador foi o número %d, com %d votos, correspondente a %.1f do total de votos.\n" %(melhor+1, votos[aux], melhorPorcentagem))
    else:
        k=0 #tamanho/quantidade de jogadores com a maior quantidade de votos
        while melhores[k]!=0:
            k+=1

        melhoresCopy=melhores[0:k]
        print(f'''\nOs melhores jogadores foram os números {melhoresCopy},''', " com %d votos cada, correspondente a %.1f do total de votos cada.\n" %( votos[aux], melhorPorcentagem))
        