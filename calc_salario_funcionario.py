''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do 
seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%.'''
 
 
salario = float(input ("informe seu salário R$: "))
 
if salario <= 1250.00 :
     
    aumento = (salario * 0.1) + salario
     

else: 
    
    aumento = (salario * 0.10) + salario
     
 
print(f"o seu salário teve um aumento de R$ {aumento:.2f}")
 
