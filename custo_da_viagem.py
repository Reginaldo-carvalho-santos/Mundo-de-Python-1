'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km
para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qaual a distancia percorrida em km:?'))
'''preço1 = 0.50
preço2 = 0.45

if distancia <= 200:
    passagem = preço1 * distancia
    print(f'O valor da passagem é R${passagem:.2f}')
else:
    passagem = preço2 * distancia
    print(f'O valor da passagem é R${passagem:.2f}')'''
    
    #outra forma de resolver 
    
if distancia <= 200:
        
        preço = distancia * 0.50
        
else:
    
        preço = distancia * 0.45
        
print(f"o valor da passagem e de: R${preço:.2f}")
    
    
    
