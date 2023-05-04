#exercicio 6

medias = []
n = 0
for i in range(10):
    notas = []
    n = n + 1
    print("notas do aluno", n)
    for j in range(4):
        
        nota = float(input("coloque a notas em ordem do aluno: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)
    
    
num_aprovados = 0

for media in medias:
    if media >= 7.0:
        num_aprovados += 1
        
print("\no numeros de aprovados é: ", num_aprovados)


