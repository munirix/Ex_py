#execicio 4

lista = []
consoantes = []
countcon = 0
for i in range(10):
    let = input("coloque uma letra: ")
    lista.append(let)
    
for letra in lista:
    if letra.lower() not in ['a', 'e','i','o','u']:
        consoantes.append(letra)
        countcon +=1
        
print("\nforam lidas ", countcon, "consoantes")
print("\nas consoantes lidas são: ", consoantes)

