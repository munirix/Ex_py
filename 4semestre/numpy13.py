import numpy as np

A = np.array([12,9,4,1,11,5,8,1,1,2,3,1]).reshape(3,-1)
print("A = \n",A)
B = np.array([1,5,1,7,1,9,1,1]).reshape(4,-1)
print("B = \n",B)

C = np.dot(A,B)
print("C = \n",C)

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

    print("\n"+"Fim Função Média".center(50,"-")+"\n")

def desvio_padrao(matriz):
    print("\n"+"Função Desvio Padrão".center(50,"-")+"\n")
    print("matriz:\n",matriz)

    # desvio padrão ao longo da coluna
    dp_coluna = np.around(np.std(matriz, axis=0))
    print("\nDesvio padrão da coluna:", dp_coluna)
    # desvio padrão ao longo da linha
    dp_linha = np.around(np.std(matriz, axis=1))
    print("\nDesvio padrão da linha:", dp_linha)

    print("\n"+"Fim Função Desvio Padrão".center(50,"-")+"\n")

matriz_media_C = media(C)
matriz_dp_C = desvio_padrao(C)

# ============= outra forma (media)=================

#row_mean = np.mean(C, axis=1) 
  
#row1_mean = row_mean[0] 
#print("média da linha 1 é", row1_mean) 
  
#row2_mean = row_mean[1] 
#print("média da linha 2 é", row2_mean) 
  
#row3_mean = row_mean[2] 
#print("média da linha 3 é", row3_mean) 
  
#column_mean = np.mean(C, axis=0) 
  
#column1_mean = np.around(column_mean[0],2)
#print("média da coluna 1 é", column1_mean) 
  
#column2_mean = np.around(column_mean[1],2)
#print("média da coluna 2 é", column2_mean) 
