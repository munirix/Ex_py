import numpy as np

A = np.array([12,9,4,1,11,5,8,1,1,2,3,1]).reshape(3,-1)
print("A = \n",A)

D = A[:,-2:]
print("D = \n",D)

def media(matriz):
    print("\n"+"Função Média".center(50,"-")+"\n")
    print("matriz:\n",matriz)

    linha,coluna = matriz.shape

    # SOMA E MEDIA DE CADA COLUNA DE UMA MATRIZ
    soma_cada_coluna = matriz.sum(axis = 0)
    media_cada_coluna = soma_cada_coluna/linha
    media_cada_coluna = np.around(media_cada_coluna,2)
    print("\nMédia de cada coluna: ",media_cada_coluna)
    
    # SOMA E MEDIA DOS ELEMENTOS DAS LINHAS DE UMA MATRIZ
    soma_cada_linha = matriz.sum(axis = 1)
    media_cada_linha = soma_cada_linha/coluna
    media_cada_linha = np.around(media_cada_linha,2)
    print("\nMédia de cada linha: ",media_cada_linha)

    soma_matriz_inteira = np.mean(D)
    print("\nMédia de toda a matriz: ",soma_matriz_inteira)

    print("\n"+"Fim Função Média".center(50,"-")+"\n")

matriz_media_D = media(D)

