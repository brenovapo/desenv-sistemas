#Usando (laços, função e try/except) crie um sistema para receber as 3 notas de um aluno
 #e calcule a media anual. Se digitar algo sem ser o numero tratar o erro.

#Usando (lista,função,laços,try/except), voce devera criar uma lista com numeros e mensagens,
# Se for numero, adicionar a uma lista a parte. Se for mensagem, tratar com o erro de tipo. Ao
# final, mostrar a lista so com os numeros

def media():
    try:

        nota1 = float(input("Nota da 1 Prova: ")) 
        nota2 = float(input("Nota da 2 Prova: ")) 
        nota3 = float(input("Nota da 3 Prova: ")) 


        media = nota1 + nota2 + nota3 /3
        print("soma:", media)
     
     
     

        
    except TypeError:
        print("Erro: - Não é possível somar tipos incompatíveis.")

    except ValueError:
        print("Erro: você digitou algo que não é um número.")

    except NameError:
        print("Erro: - Variável não definida.")


media()a



