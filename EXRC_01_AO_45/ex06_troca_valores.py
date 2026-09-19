#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

A = int(input("Infome o valor A para ser feito a troca: "))
B = int(input("Infome o valor B para ser feito a troca: "))

troca = A
A = B
B = troca 

print(f"O valor de A após a troca é: {A}")
print(f"O valor de B após a troca é: {B}")