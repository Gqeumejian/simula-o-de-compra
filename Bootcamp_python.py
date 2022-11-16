from ast import If
from cmath import exp
from lib2to3.pytree import type_repr

#Simulacao de compra em maquininha de cartao 

saldo = 500
compra = int(input("Insira o valor da compra:"))
cheque_especial = 2000
conta_especial = True
saldo_atual = saldo - compra

if saldo >= compra: 
    print("Pagamento aprovado")
else: 
    print("Saldo em conta corrente insuficiente")

exp_1 = compra >= saldo and compra <= cheque_especial or conta_especial >= saldo
valor_conta_corrente = compra 
valor_cheque_especial = compra - saldo

if exp_1:
    print('Cheque especial utilizado')
else:
    print("Valor debitado em conta corrente")

if saldo <= compra_14_11_2022:
    print ('O valor utilizado do seu cheque especial e de:',abs(valor_cheque_especial))
else:
    print('O valor debitado da conta corrente e de:', abs(valor_conta_corrente))

