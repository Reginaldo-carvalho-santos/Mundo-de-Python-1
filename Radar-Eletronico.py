'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = float(input('qual é a velocidade atual do carro: '))

multa = (7*(vel - 80))
#limite = 80
#custo = ((vel - limite) * multa)

if vel > 80 :
    
    print(f'Vc ultrapassou o limite de velocidade de 80km 🚓 , vc foi multado em :R${multa:.2F}')
    
print('TENHA UM BOM DIA! Dirija com cuidado')  