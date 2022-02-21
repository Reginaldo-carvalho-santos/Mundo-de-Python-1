# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('descubra se o número e par ou impar: '))

resultado = num % 2

if resultado == 0:
    print(f'o numero {num} e par. ')
else:
    print('o numero e impar.')
