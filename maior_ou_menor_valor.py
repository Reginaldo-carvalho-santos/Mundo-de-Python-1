'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
print('-='*30)
print(' Qual é o maior e menor valor?:')
print('-='*30)

a = int(input(' Digite o primeiro número:'))
b = int(input(' Digite o  segundo número:'))
c = int(input('Digite o terceiro número: '))

menor = a
maior = b

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and a > c:
    maior = b
if c > b and c > a :
    maior = c    
    
print(f"o menor numero e {menor} e o maior numero e {maior}")