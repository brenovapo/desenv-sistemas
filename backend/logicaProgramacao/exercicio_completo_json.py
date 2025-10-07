#crie um sistema de gerenciamento de petshop
#devera ter os campos: nome, raça, idade, sexo, nome_dono, telefone_dono
#o nome do arquivo json deve ser "petshop.json"
#faça o crud complexo
#ao terminar, demonstrar o exercicio pro professor

import json 

inventario = []
#lendo o comentario
try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado")

try:
    id= int(input("digite o id do pet: "))
    nome= input ("digite o nome do pet: ")
    raca= input ("digite a raça do pet: ")
    idade= int (input("digite a idade do pet "))
    sexo= input ("digite o sexo do pet: ")
    nome_dono= input ("digite o seu nome: ")
    telefone_dono= input("digite o seu número: ")

except ValueError:
    print("Digite o valor corretamente")


novo_pet= {"id" : id,
    "nome" : nome,
    "raca" : raca,
    "idade": idade,
    "sexo": sexo,
    "nome_dono": nome_dono,
    "telefone_dono": telefone_dono,
    }

inventario.append(novo_pet)
with open ("petshop.json", "w") as arquivo:
    json.dump(inventario, arquivo, indent = 4)

print("pet cadastrado")


#modificar pet

pet_encontrado= False 
id_pet_modificar = int(input("Digite o id para modificar: "))
novo_nome= input("Digite o novo nome: ")
novo_raca= input("Digite a nova raça: ")
novo_idade= int(input("Digite a nova idade: "))
novo_sexo= input("Digite o novo sexo: ")

for pet in inventario:
    if pet['id'] == id_pet_modificar:
        #colocamos a nova quantidade
        pet['nome'] = novo_nome
        pet['raca'] = novo_raca
        pet['idade'] = novo_idade
        pet['sexo'] = novo_sexo
        pet_encontrado = True 
        break;

if not pet_encontrado:
    print("o pet com o id informado não foi encontrado")

else:
    with open ("petshop.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent = 4)
    print("o arquivo foi alterado com sucesso!!")


#listar pet do arquivo json
    
try:
    with open ("petshop.json",'r') as arquivo:
        inventario= json.load(arquivo)

    if not inventario:
        print("O arquivo está vazio!")

    else:
        print("----- Lista de pets cadastrados -----")
        for pet in inventario:
            print(f"\n-- Pet {pet.get('id')} --")
            print(f"Nome: {pet.get('nome', 'n/a')}")
            print(f"Raça: {pet.get('raca', 'n/a')}")
            print(f"Sexo: {pet.get('sexo', 'n/a')}")
            print(f"Idade: {pet.get('idade', 0)} anos")
            print(f"Nome do dono: {pet.get('nome_dono', 'n/a')}")
            print(f"Telefone do dono: {pet.get('telefone_dono', 'n/a')}")

except FileNotFoundError:
    print("arquivo não encontrado")



#excluir pet no json

try:
    with open("petshop.json", "r") as arquivo:
        inventario = json.load(arquivo)

except FileNotFoundError:
    print("Arquivo não encontrado")


novo_inventario = []
pet_excluido = False

id_pet_excluir = int(input("digite o  id do pet para excluir: "))

for pet in inventario:
    if pet["id"] != id_pet_excluir:
    #se o id for diferente adicionamos  a nova lista 
        novo_inventario.append(pet)
    else:
        print("pet removido com sucesso!!")
        pet_excluido = True

else:
    with open('petshop.json', 'w') as arquivo:
        json.dump(novo_inventario, arquivo, indent=4)
        print('o arquivo foi atualizado, pet removido')









    




    