#Quando se tem mais de um atributo (ou variável) para cada registro, o uso de arquivos 
#.txt simples torna-se complicado porque esses arquivos não possuem uma estrutura definida 
#para organizar os dados. Isso significa que é necessário criar uma forma manual de separar os atributos,
#como por exemplo usando vírgulas, espaços ou tabulações. No entanto, isso pode causar problemas, 
#especialmente quando os próprios valores contêm esses mesmos caracteres, 
#o que dificulta a separação correta dos dados. Além disso, como tudo é armazenado como texto puro, 
#não há controle de tipos (como números, datas ou textos), o que exige conversões manuais durante a 
#leitura e aumenta a chance de erros. Com muitos atributos, a leitura, escrita, busca e atualização 
#das informações se tornam processos lentos e propensos a falhas, já que é necessário processar todo 
#o arquivo linha por linha. Essa falta de estrutura, validação e eficiência torna arquivos .txt pouco 
#adequados para armazenar dados complexos ou em grande volume, sendo preferível o uso de formatos mais 
#estruturados como CSV, JSON ou bancos de dados.