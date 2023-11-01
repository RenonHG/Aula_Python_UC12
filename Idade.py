#verificar idade do usuario
#menor que 8 anos -> bebe
#entre 8 e 13 -> criança
#entre 14 e 20 -> adolescente
#entre 21 e 64 -> adulto
#maior que 65 -> idoso

idade = int(input("Insira sua idade: "))

if(idade < 8):
    print("Você é bebê!")

elif(idade >= 8 and idade <= 13):
    print("Você é criança!")

elif(idade >= 14 and idade <= 20):
    print("Você é adolescente!")

elif(idade >= 21 and idade <= 64):
    print("Você é adulto!")

elif(idade >= 65 and idade <= 120):
    print("Você é idoso!")

else:
    print("Você é provavelmente é um Vampiro!")

