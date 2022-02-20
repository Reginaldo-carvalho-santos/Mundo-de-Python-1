'''Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import choice

num = int(input('informe um numero: '))

lista = [0,1,2,3,4,5]

computador = choice(lista)

if num == computador:
    
    print('o numero sorteado foi {} e seu foi {}'.format(num,computador))
    print('Parabéns,vc acertou!')
    
else :
    print('vc perdeu! tente de novo')
    print('o numero sorteado foi {} e seu foi {}'.format(computador,num))

