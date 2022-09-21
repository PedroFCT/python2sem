

dicionario = {"nome" : ["Danilo"]}
print(dicionario["nome"])
dicionario["data"] = ["18/09/2029"]
print(dicionario)
dicionario["nome"].append("Vinicius")
print(dicionario["nome"])

#crie um dicionario com nomes de carros e o ano do carro em cada chave

carros={}
carros["Marca"]=["Hiunday", "Mascerati"]

print(carros["Marca"])

#crie um dicionario com nomes seleções e o numero de copas que ela ganhou


copas={"selecoes" : ["Brasil", "Camarões", "Gana", "Gales", "EUA", "Canada", "França", "Holanda", "Alemanha"]}
copas["copasVencidas"]= ["6 fds", "0", "0", "0", "0", "0", "2", "0", "4"]
print(copas)

#############################################################

def gera_par_impar(dicionarioParImpar):
    for i in range(10):
        if num%2==0:
            dicionarioParImpar["par"].append["par"]
        else:
            dicionarioParImpar["impar"].append["impar"]

num=[2, 3, 6, 19, 1, 31]

def find_maior_menor(lista):
    numeros= {"maior" : None, "menor" : None, "média" : None}
    numeros["maior"] = max(lista)
    numeros["menor"] = min(lista)
    numeros["média"] = sum(lista)/len(lista)
    return numeros

print(find_maior_menor(num))

##########################################################

frase = "abobora cadente estrela abobora vulcao copa found"

def find_and_count(frase):
    
    contadorRep=0
    
    frase = frase.lower()
    frase = frase.replace(",", '')
    frase = frase.replace(".", '')
    
    palavra=input("Digite a palavra que deseja encontrar: ")
    if palavra in frase:

######################################################################


    








