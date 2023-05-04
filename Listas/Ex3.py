#Exercicio 3

lista = []


x = input("coloque o primeiro nota: ")
x = float(x)
lista.append(x)
y = input("coloque o segundo nota: ")
y = float(y)
lista.append(y)
z = input("coloque o terceiro nota: ")
z = float(z)
lista.append(z)
f = input("coloque o quarto nota: ")
f = float(f)
lista.append(f)

print("\nas notas são: ",lista)


media = sum(lista) / len(lista)

print("\na média é: ", media)