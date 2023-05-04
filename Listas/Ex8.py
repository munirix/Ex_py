#exercicio 8

idades = []
alturas = []
n = 0
for j in range(5):
    n = n + 1
    print("sobre a pessoa", n)
    for i in range(1):
      idade = int(input("digite a idade dela: "))
      altura = float(input("digite a altura dela: "))
      idades.append(idade)
      alturas.append(altura)
     
      

print("idades em ordem inversa: ")
for i in range(4, -1, -1):
    print(idades[i])
    
print("alturas em ordem inversa: ")
for i in range(4,-1,-1):
    print(alturas[i])
    