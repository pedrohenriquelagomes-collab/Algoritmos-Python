#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor por horas tranalhadas: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
num_dependentes = int(input("Digite o numero de dependentes: "))

salario_bruto = horas_trabalhadas * valor_hora
valor_desconto = salario_bruto * percentual_desconto /100
bonus_dependentes = num_dependentes * 100

salario_liquido = salario_bruto - valor_desconto + bonus_dependentes

print(f"\n--- Demonstrativo de Pagamento ---")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Acréscimo por dependentes: R$ {bonus_dependentes:.2f}")
print(f"Salário a receber: R$ {salario_liquido:.2f}")