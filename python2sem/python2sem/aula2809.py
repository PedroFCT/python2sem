dicionarioNomes= {"nome" : "Danilo"} 

print(dicionarioNomes["nome"]) 

dicionarioNomes["sobrenome"] = "elias" 

print(dicionarioNomes) 

dicionarioNomes["nome"]="caio" 

print(dicionarioNomes) 

dicionarioNomes["nome"]=[dicionarioNomes["nome"]] 

print(dicionarioNomes) 

dicionarioNomes["nome"].append("Vinicius") 

print(dicionarioNomes) 

print(dicionarioNomes.keys()) 

 
 

for key in dicionarioNomes.keys(): 

    print(key) 

 
 

######################################################################################### 

    

#crie um dicionario com as chaves carro, ano e preço e preencha com 5 carros 

#crie uma função que encontra o carro mais caro e o carro mais barato 

#crie uma função que encontra o carro mais velho e o carro mais novo 

  

dicioCarro= {"carros":["Golf GTI", "Duster", "Jeta", "Velar", "Marea"], "ano": [2022, 2010, 1979, 2021, 1998], "preco": [150000, 104200, 215230, 613950, 4043]} 

 
 

def caro_barato(dicionario): 

    indiceMenor=0 

    indiceMaior=0 

    menorValor= dicionario["preco"][0] 

    maior_valor=dicioCarro["preco"][0] 

    for i in range(len(dicionario["preco"])): 

      if dicionario["preco"][i]<menorValor: 

          menorValor=dicionario["preco"][i] 

          indiceMenor=i 

          carroMaisBarato=dicionario["carros"][indiceMenor] 

     

    for i in range(len(dicionario["preco"])): 

      if dicionario["preco"][i]>maior_valor: 

          maior_valor=dicionario["preco"][i] 

          indiceMaior=i 

          carroMaisCaro=dicionario["carros"][indiceMaior] 

           

           

    print(f"O carro mais barato registrado é o {carroMaisBarato} e custa: R${menorValor}") 

    print(f"O caro mais caro registrado é o {carroMaisCaro} e custa: R${maior_valor}" ) 

    return menorValor 

 
 

def novo_velho(dicionario): 

    indiceMenor=0 

    indiceMaior=0 

    maisNovo= dicionario["ano"][0] 

    maisVelho=dicionario["ano"][0] 

     

    for i in range(len(dicionario["ano"])): 

      if dicionario["ano"][i]<maisNovo: 

          maisNovo=dicionario["ano"][i] 

          indiceMenor=i 

    carroMaisNovo=dicionario["carros"][indiceMenor] 

     

    for i in range(len(dicionario["preco"])): 

      if dicionario["ano"][i]>maisVelho: 

          maisVelho=dicionario["ano"][i] 

          indiceMaior=i 

    carroMaisVelho=dicionario["carros"][indiceMaior] 

           

           

    print(f"O carro mais velho registado é o {carroMaisNovo} do ano {maisNovo}") 

    print(f"O carro mais novo registrado é o {carroMaisVelho} do ano {maisVelho}") 

    return  

 
 

print(novo_velho(dicioCarro)) 

print(caro_barato(dicioCarro)) 

 
 

#crie um dicionario com as chaves "arroz" e seu preço como valor (por exemplo) 

#de ao usuario opções do que ele pode comprar e pergunte quantos itens no total 

#faça um for na qtd de items, receba o nome do produto que ele quer comprar 

#printe no fim o total gasto pelo cliente 

 
 

dicioProdutos={"produtos" : ["ARROZ", "FEIJAO", "BANANA", "TOMATE", "PRESUNTO"], "precos" : [10.40, 7.99, 2.99, 1.50, 3.99]} 

print(dicioProdutos) 

 
 

selecaoProduto=input("Digite o produto que deseja comprar: ").upper 

quantidade=input("Seleciona a quantidade que deseja comprar: ") 