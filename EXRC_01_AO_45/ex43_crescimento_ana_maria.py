# Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

ana = 1.10
maria = 1.50
taxa_ana = 0.03
taxa_maria = 0.02

for anos in range(1, 101):
    ana += taxa_ana
    maria += taxa_maria

    if ana > maria:
        print(f"Serão necessários {anos} anos para que Ana seja maior que Maria.")
        print(f"Altura final - Ana: {ana:.2f}m | Maria: {maria:.2f}m")
        break
