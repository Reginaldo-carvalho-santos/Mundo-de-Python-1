'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = float(input('iforme a velocidade: '))

multa = 7
limite = 80
custo = ((vel - limite) * multa)

if vel > 80 :
    
    print(f'o vc ultrapassou o limite de velocidade de {limite}km, vc foi multado em :R${custo:.2F}')

else:
    print('')  