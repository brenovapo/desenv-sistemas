
nota1 = int (input("Digite sua nota "))
nota2 = int (input("Digite sua nota "))
nota3 = int (input("Digite sua nota "))
nota4 = int (input("Digite sua nota "))
notafinal = (nota1 + nota2 + nota3 + nota4) / 4

print("Sua nota foi", notafinal)

if (nota1 >= 80):
        print("Execelente")
elif(nota1 < 80 and nota1 >= 60):
        print("Passou")
elif(nota1 < 60):
        print ("Até ano que vem")

     