#exercicio 5


lista_vetor = []
listapar = []
listaimp = []

for i in range(20):
    num = float(input("digite um numero: "))
    lista_vetor.append(num)

    if num % 2 ==0:
        listapar.append(num)
    else:
        listaimp.append(num)
        
print("o vetor completo é: ", lista_vetor)
print("\no vetor de numeros pares são: ", listapar)
print("\no vetor de numeros impares: ", listaimp)



