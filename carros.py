fileCar = "carros_cadastrados.txt"

def converter_file_em_dicionario():
    # Essa função é chamada sempre qie for necessário trazer os dados do .txt para dicionário
    carros_cadastrados_do_arquivo = []

    try:
        # Convertendo de String para um dicionário
        with open(fileCar, "r") as file:
            for line in file:
                carros_cadastrados_do_arquivo.append(eval(line)) 
            return carros_cadastrados_do_arquivo
    except:
        return
    
    
    

def cadastrar_os_carros_pioneiros():
    # Essa função vai cadastrar os 20 primeiros carros do .txt
    
    # Lista dos carros que são padrão no .txt
    carros_pioneiros = [
        {"nome": "Honda Civic", "preco": 61200, "ano": 2017, "estado": "novo"},
        {"nome": "Toyota Corolla", "preco": 66000, "ano": 2020, "estado": "seminovo"},
        {"nome": "Ford Mustang", "preco": 54500, "ano": 2019, "estado": "conservado"},
        {"nome": "Chevrolet Camaro", "preco": 65400, "ano": 2021, "estado": "conservado"},
        {"nome": "Volkswagen Golf", "preco": 31420, "ano": 2015, "estado": "seminovo"},
        {"nome": "Fiat Uno", "preco": 24500, "ano": 2018, "estado": "mal estado"},
        {"nome": "Hyundai Tucson", "preco": 36000, "ano": 2022, "estado": "conservado"},
        {"nome": "Jeep Renegade", "preco": 70900, "ano": 2020, "estado": "novo"},
        {"nome": "Nissan Sentra", "preco": 34000, "ano": 2018, "estado": "mal estado"},
        {"nome": "BMW Serie 3", "preco": 45000, "ano": 2014, "estado": "conservado"},
        {"nome": "Mercedes-Benz Classe C", "preco": 12000, "ano": 2009, "estado": "seminovo"},
        {"nome": "Chevrolet Onix", "preco": 99060, "ano": 2010, "estado": "novo"},
        {"nome": "Renault Sandero", "preco": 17020, "ano": 2011, "estado": "mal estado"},
        {"nome": "Peugeot 208", "preco": 24200, "ano": 2014, "estado": "seminovo"},
        {"nome": "Kia Sportage", "preco": 32000, "ano": 2012, "estado": "seminovo"},
        {"nome": "Volvo XC60", "preco": 31400, "ano": 2013, "estado": "conservado"},
        {"nome": "Land Rover Discovery", "preco": 25400, "ano": 2020, "estado": "mal estado"},
        {"nome": "Tesla Model S", "preco": 79400, "ano": 2024, "estado": "novo"},
        {"nome": "Porsche 911", "preco": 110200, "ano": 2012, "estado": "novo"},
        {"nome": "BMW Serie 1", "preco": 92200, "ano": 2010, "estado": "mal estado"}
    ]

    # Aqui pegamos os carros já cadastrados para uma checagem
    carros_cadastrados = converter_file_em_dicionario()

    # Caso não hajam carros cadastrados, iremos cadastrar os carros pioneiros
    if(type(carros_cadastrados) == None):
        for carro in carros_pioneiros:
            with open(fileCar, "a") as file:
                file.write(str(carro) + "\n")
    else:
        if(len(carros_cadastrados) == 0):
            for carro in carros_pioneiros:
                with open(fileCar, "a") as file:
                    file.write(str(carro) + "\n")

def buscar_carros(pesquisa):
    # Essa função vai buscar os carros com base no valor que o usuário usou

    carros_adequados = []
    
    try:
        # Aqui o programa tenta converter o valor que o usuário digitou para um float
        # caso consiga, quer dizer que o valor que ele digitou é um float.

        pesquisa = float(pesquisa)
        print("O valor fornecido é um float" + "\n")

        # Abrir o .txt e procurar os carros cujo preço seja menor ou igual ao preço que o usuário digitou
        carros = converter_file_em_dicionario()

        for carro in carros:
            if(carro['preco'] <= pesquisa):
                carros_adequados.append(carro)
        
        return carros_adequados

    # Bloco de código caso o usuário digite uma string
    except:
        

        estados_dos_carros = ["novo", "seminovo", "conservado", "mal estado"]
        pesquisaAdequada = False
        
        # Checar se a string fornecida é adequada, ou seja, se ela é um dos possíveis estados para o carro.
        for estado in estados_dos_carros:
            if(estado == pesquisa): 
                pesquisaAdequada = True
                break

        # Caso o valor digitado pelo usuária(a string) for adequada, ele vai rodar esse bloco de código
        if(pesquisaAdequada):
            carros = converter_file_em_dicionario()

            print(f"O estado do carro é {pesquisa}")

             # Aqui vai está onde vou segregar os carros a partir do estado deles
            for carro in carros:
                if(carro['estado'] == pesquisa):
                    carros_adequados.append(carro)

            return carros_adequados

        else:

            # Aqui eu quero fazer ele voltar para o menu quando ele errar. 

            print("O valor inserido foi inválido, tente novamente")
            return
            # Retornar pro main / menu

def cadastrar_carros(nome: str, preco: float, ano: int, estado: str): 
    car = {'nome': nome, 'preco': preco, 'ano': ano, 'estado': estado}

    with open(fileCar, "a") as file:
        file.write(str(car) + "\n") 

    continue_loop = input("Deseja continuar (s / n): ").lower()

    return continue_loop

def menu():
    print("================ Bem vindo! ================")
    print("[0] - [\U0001F50E Buscar Carro ]")
    print("[1] - [\U0001F4DD Cadastrar um novo carro ]")
    print("[2] - [\u274C Sair ]")
    print("============================================")

    number = int(input("Qual opção você deseja: "))
    return number

def main():

    cadastrar_os_carros_pioneiros() # Aqui o programa cadastra os primeiros 20 carros
    
    number = menu()
    
    match number:
        case 0:
            # buscar carro
            pesquisa = input("Um valor máximo ou uma string: ")
            carros_adequados = buscar_carros(pesquisa)

            if(len(carros_adequados) == 0):
                print("Não foram encontrados carros")
            else:
                for carro in carros_adequados:
                    print(f"Nome: {carro['nome']}, Preço: {carro['preco']}, Ano: {carro['ano']}, Estado: {carro['estado']}" + "\n")
        case 1:
            # cadastrar um novo carro
            manter_loop = "s"

            while(manter_loop == "s"):
                nomeUser = input("Qual o nome do carro: ")
                preco = float(input("Qual o preço do carro: "))
                ano = int(input("Qual o ano do carro: "))
                estado = input("Qual o estado do carro(novo, seminovo, conservado, mal estado)").lower()
                manter_loop = cadastrar_carros(nomeUser, preco, ano, estado)
            
main()
