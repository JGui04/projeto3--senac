"""
Criar um programa após a entrada do nome, cargo, salario bruto, calcule i INSS 
até 1412 - 7.5%
até 2666.68 - 9%
até 4000.03 - 12%
até 7786.02 - 14%
acima fixo em 1200.00 // não sei se é real

Caso o usuario tenha dependentes ele deve informar o nome de cada dependente menor que 18 anos até 21 anos caso esteja na faculdade ou deficiente. 
Conjugue que tenha renda inferior a 27mil por ano entra como dependente.
"""

nome = str(input("Escreva seu nome:\n"))
cargo = str(input("\nEscreva seu cargo:\n"))
salarioBruto = float(input("\nDigite seu salário:\n"))

s1 = salarioBruto*0.075
s2 = salarioBruto*0.9
s3 = salarioBruto*0.12
s4 = salarioBruto*0.14
s5 = salarioBruto*1200



if salarioBruto <= 1412:
    inss = s1
elif salarioBruto > 1412 or salarioBruto < 2666.68:
   inss = s2
elif salarioBruto > 2666.68 or salarioBruto < 4000.03:
    inss = s3

elif salarioBruto > 4000.03 or salarioBruto < 7786.02:
    inss = s4
else:
    inss = s5

dpC = int(input("Dependente conjugue renda anual até 27mil:\n1 - sim\n2 - não\n"))

while(dpC < 1 or dpC > 2):
    print("Erro - valor de entrada inválido!!")
    dpC = int(input("Depemdemte conjugue renda anual até 27mil:\n1 - sim\n2 - não\n"))

while (dpC == 1):
    nomeC = str(input("Digite o nome do conjugue:\n"))

    dpC = 2