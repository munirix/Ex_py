'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as
quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''
print('''Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00''')
print('\nDigite 0 no código para sair\n')
total=0
while True:
    
    codigo = int(input('Digite o código: '))
    if codigo == 0:
        break
    quantidade = int(input('Digite a quantidade: '))

    if codigo == 100:
        print('Cachorro Quente %.2f' %(quantidade * 1.20))
        total+=quantidade * 1.20
    if codigo == 101:
        print('Bauru Simples %.2f' %( quantidade * 1.30))
        total+=quantidade * 1.30
    if codigo == 102:
        print('Bauru com ovo %.2f' %( quantidade * 1.50))
        total+=quantidade * 1.50
    if codigo == 103:
        print('Hambúrguer %.2f' %( quantidade * 1.20))
        total+=quantidade * 1.20
    if codigo == 104:
        print('Cheeseburguer %.2f' %( quantidade * 1.30))
        total+=quantidade * 1.30
    if codigo == 105:
        print('Refrigerante %.2f' %( quantidade * 1.00))
        total+=quantidade
print('\n-------------------------\nTotal do pedido: %.2f'%(total))
