#Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os
#quais fornece a quantidade de ração em gramas. A quantidade diária de ração
#fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do
#saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre
#quanto restará de ração no saco após cinco dias.



pesoSaco=int(input("Qual o peso da ração? "))
quantidadeRacao=int(input("Qual a quantidade de ração? "))
quanatidadeEmgramas=pesoSaco*1000
quantidade=quanatidadeEmgramas/quantidadeRacao

dias=quantidade*5

print("Restará apenas isso de ração ",dias)
