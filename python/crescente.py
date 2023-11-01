# colete 3 numeros do usuario, e apos isso os ordene em ordem CRESCENTE
# && >>>>> and
# || >>>>> or

print("Digite 3 valores inteiros: ")

n1 =  (input("\nInsira o primeiro: "))
n2 =  (input("Insira o segundo: "))
n3 =  (input("Insira o terceiro: "))

print ("\nValor A: " + n1 + " | Valor B: "+ n2 +" | Valor C: " + n3)

# primeiro 
if (n1 < n2 and n1 < n3):
    print ("1º " , n1)

elif(n2 < n1 and n2 < n3):
    print("1º " , n2)

elif(n3 < n1 and n3 < n2):
    print("1º " , n3)

# segundo 
if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print ("2º " , n1)

elif(n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3):
    print("2º " , n2)

elif(n3 > n1 and n3 < n2) or (n3 < n1 and n3 > n2):
    print("2º " , n3)

#terceiro
if (n1 > n2 and n1 > n3):
    print ("3º " , n1)

elif(n2 > n1 and n2 > n3):
    print ("3º " , n2)

elif(n3 > n1 and n3 > n2):
    print ("3º " , n3)





# print ("\nOrdem Crescente:")
# print ("\Menor: " + t1 + " | Meio: "+ t2 +" | Maior: " + t3)