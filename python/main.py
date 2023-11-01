print ("Hello World")
# hashtag para comentário
# colete 3 valores do usuario (a, b, c) e troque os seguintes valore:
# a = b
# b = c
# c = a
#imprima na tela os resultados.

a =  (input("Insira o valor A: "))
b =  (input("Insira o valor B: "))
c =  (input("Insira o valor C: "))

print ("\nValor A: " + a + "\nValor B: "+ b +"\nValor C: " + c)

temp = a
a = b
b = c
c = temp

print ("\nNovos valores: ")
print ("Valor A: " + a + " | Valor B: "+ b +" | Valor C: " + c)
