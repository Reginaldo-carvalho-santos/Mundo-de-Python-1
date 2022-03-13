'''Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo.

formula usada:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

'''

reta_A = float(input("\033[7;33;minforme o tamanho das retas: "))
reta_B = float(input("informe o tamanho das retas: "))
reta_C = float(input("informe o tamanho das retas: "))

if reta_A < reta_B + reta_C and reta_B < reta_C + reta_A and reta_C < reta_A + reta_B:
    
    print(f"As retas A= {reta_A}, B= {reta_B} e C= {reta_C} podem formar um triangulo ")

else:
    
    print("as retas não podem formar um triangulo")