# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

print ('{:=^40}'.format('LOJAS BORGES'))

preco = float (input('Informe o preço das compras: R$'))

print (''' FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')

opção = int (input('Digite a sua opção:'))

if opção == 1:
    total = preco (preco * 10/100)

elif opção == 2:
    total = preco - (preco * 5/100)
    
elif opção == 3:
    total = preco
    parcelas = total / 2
    print ('Sua compra será parcelada em 2x de R$ {:.2f}'.format (parcelas))

elif opção == 4:
    total = preco + (preco * 20/100)
    totparc = int (input ('Quantas parcelas?'))
    parcelas = total / totparc 
    print ('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcelas))

else: total = preco 

print ('OPÇÃO INVALIDA DE PAGAMENTO.')
print ('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format (preco, total))
