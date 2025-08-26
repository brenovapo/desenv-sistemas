def filtrar_numeros(lista_mista):
    numeros = []
    
    for item in lista_mista:
        try:
           
            resultado = item * 1
            numeros.append(item)
        except TypeError:
            print("Ignorando valor não numérico:")
    
    return numeros

lista_original = [10, "Olá", 25, "Erro", 42, "Mensagem", -7, 3.14, "Fim"]

lista_numeros = filtrar_numeros(lista_original)

print("Lista com apenas números:", lista_numeros)