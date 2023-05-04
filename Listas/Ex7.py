#exercicio 7

vetor = []

for i in range(5):
    num = int(input("coloque um numero: "))
    vetor.append(num)
    
soma = sum(vetor)
mult = 1
for num in vetor:
    mult *= num
    
print("os numeros são: ", vetor)
print("a soma é: ", soma)
print("a multiplição é: ", mult)
