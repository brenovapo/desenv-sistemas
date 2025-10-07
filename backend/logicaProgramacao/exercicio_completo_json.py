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
    id= int(input("digite o id do produto"))
    nome= input ("digite o nome do pet: ")
    raca= input ("digite a raça do pet: ")
    idade= int (input("digite a idade do pet "))
    sexo= input ("digite o sexo do pet: ")
    nome_dono= input ("digite o seu nome: ")
    telefone_dono= input (input("digite o seu número: "))

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

id_pet_modificar = int(input("Digite o id para modificar"))
novo_nome




for pet in inventario:
    if pet['id'] == id_pet_modificar:
        pet['quantidade'] = nova_quantidade
        pet['em_estoque'] = nova_quantidade
        pet = True 
        break;
if not produto_encontrado:
    print("o produto com o id informado não foi encontrado")

else:
    with open ("petshop.json", "w") as arquivo
        json.dump(inventario, arquivo, ident = 4)
    print("o arquivo foi alterado com sucesso!!")






    




    