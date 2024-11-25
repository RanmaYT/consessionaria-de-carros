import os
import time

fileName = "carros_cadastrados.txt"

def criar_file():
    # Checa se o arquivo já existe, caso não, cadastra os carros pioneiros
    try:
        with open(fileName) as file:
            file.read()
    except FileNotFoundError:
        cadastrar_os_carros_pioneiros()

def cadastrar_os_carros_pioneiros():
    # Cria o arquivo e salva os dados dos carros pioneiros.
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
        {"nome": "BMW Série 3", "preco": 45000, "ano": 2014, "estado": "conservado"},
        {"nome": "Mercedes-Benz Classe C", "preco": 12000, "ano": 2009, "estado": "seminovo"},
        {"nome": "Chevrolet Onix", "preco": 99060, "ano": 2010, "estado": "novo"},
        {"nome": "Renault Sandero", "preco": 17020, "ano": 2011, "estado": "mal estado"},
        {"nome": "Peugeot 208", "preco": 24200, "ano": 2014, "estado": "seminovo"},
        {"nome": "Kia Sportage", "preco": 32000, "ano": 2012, "estado": "seminovo"},
        {"nome": "Volvo XC60", "preco": 31400, "ano": 2013, "estado": "conservado"},
        {"nome": "Land Rover Discovery", "preco": 25400, "ano": 2020, "estado": "mal estado"},
        {"nome": "Tesla Model S", "preco": 79400, "ano": 2024, "estado": "novo"},
        {"nome": "Porsche 911", "preco": 110200, "ano": 2012, "estado": "novo"},
        {"nome": "BMW Série 1", "preco": 92200, "ano": 2010, "estado": "mal estado"}
    ]

    for carro in carros_pioneiros:
        with open(fileName, "a", encoding = "utf-8") as file:
            file.write(str(f"{carro['nome']}, {carro['preco']}, {carro['ano']}, {carro['estado']} \n"))

def temporaryMessage(message: str, timer: float):
    
    print(message)
    time.sleep(timer)

def converter_file_em_dicionario():
    # Pega os dados do arquivo txt e converte para estrutura de dicionário e por fim retorna esse dicionário.
    carros_cadastrados_do_arquivo = []

    with open(fileName, "r") as file:
        for line in file:
            # Para cada linha ele tira os espaços, separa os elementos com base na "," e aloca eles em uma variável local no estilo de dicionário.
            line = line.strip()
            lineElements = line.split(",")
            car = {'nome': lineElements[0], 'preco': float(lineElements[1]), 'ano': int(lineElements[2]), 'estado': lineElements[3].strip()}
            carros_cadastrados_do_arquivo.append(car)
            
    return carros_cadastrados_do_arquivo

def buscar_carros(o_que_buscar):
    carros = converter_file_em_dicionario()

    while True:
        
        os.system("cls")

        match o_que_buscar.lower():
            case "nome":
                nome = input("📛 Digite o nome do carro: ").lower()
                carros_filtrados = [carro for carro in carros if nome in carro['nome'].lower()]
                break
            case "ano":
                ano = int(input("🗓️ Digite o ano do carro: "))
                carros_filtrados = [carro for carro in carros if carro['ano'] == ano]
                break
            case "preco":
                preco_max = float(input("💵 Digite o preço máximo: "))
                carros_filtrados = [carro for carro in carros if carro['preco'] <= preco_max]
                break
            case "estado":
                estado = input("📋 Digite o estado do carro (novo, seminovo, conservado, mal estado): ").lower()
                carros_filtrados = [carro for carro in carros if carro['estado'] == estado]
                break
            case _:
                temporaryMessage("Por favor, digite um valor válido", 1.5)

    temporaryMessage("Carregando os carros disponíveis...", 4)

    return carros_filtrados

def buscar_carros_menu():

    os.system("cls")

    print("================ Buscar Carros ================")
    print("[1] - 📛 Buscar por Nome")
    print("[2] - 🗓️ Buscar por Ano")
    print("[3] - 💵 Buscar por Preço maximo")
    print("[4] - 📋 Buscar por Estado")
    print("[0] - 🔙 Voltar ao Menu Principal")
    print("===============================================")

    while True:
        try:
            opcao = int(input("Escolha uma opção de busca: "))

            match opcao:
                case 0:
                    return
                case 1:
                    carros_aprovados = buscar_carros("Nome")
                case 2:
                    carros_aprovados = buscar_carros("Ano")
                case 3:
                    carros_aprovados = buscar_carros("Preco")
                case 4:
                    carros_aprovados = buscar_carros("Estado")

            if(type(carros_aprovados) != None):
                return carros_aprovados

        except ValueError:
            print("⚠️Opa, parece que você digitou um valor errado. Tente novamente utilizando os valores certos.")

def cadastrar_carros(nome: str, preco: float, ano: int, estado: str):
    car = {'nome': nome, 'preco': preco, 'ano': ano, 'estado': estado}

    with open(fileName, "a", encoding = "utf-8") as file:
        file.write(str(f"{car['nome']}, {car['preco']}, {car['ano']}, {car['estado']} \n"))

    print("✅ Carro cadastrado com sucesso!")

def printCarDisponible(carros_adequados):
    
    os.system("cls")

    # botar um if pra ver se a pessoa quer continuar procurando carros ou não. Se ela botar sim, vai voltar ao menu de buscar carros.
    if (len(carros_adequados) == 0):
        print("Não há carros adequados")
        
    else:
        os.system("cls")
        for carro in carros_adequados:
            print(f"🏷️  Carro: {carro['nome']} \n  💲 Preço: {carro['preco']} \n  🗓️  Ano: {carro['ano']} \n  🚨 Estado: {carro['estado']} \n")

def menu_principal():
    
    os.system("cls")

    while True:
        try:
            os.system('cls')
            print("================ Bem vindo! ================")
            print("[0] - [🔍 Buscar Carro ]")
            print("[1] - [📝 Cadastrar um novo carro ]")
            print("[2] - [❌ Sair ]")
            print("============================================")

            number = int(input("Qual opção você deseja: "))
            return number
        
        except ValueError:
            os.system('cls')
            temporaryMessage("⚠️ Por favor, use apenas números", 1.5)
    
def main():
    try:
        criar_file()

        number = menu_principal()

        while True:
            
            match number:
                case 0:
                    carros = buscar_carros_menu()
                    if(carros != None):
                        printCarDisponible(carros)
                    else:
                        number = menu_principal()
                        continue
                case 1:
                        os.system("cls")
                        try:
                            # Pegar as informações do carro
                            carro_nome = input("Qual o nome do carro: ")
                            carro_preco = float(input("Qual o preço do carro: "))
                            carro_ano = int(input("Qual o ano do carro: "))
                            carro_estado = input("Qual o estado atual do carro (novo, seminovo, conservado, mal estado): ").lower()

                            # fazer verificação (ano e preço não podem ser negativos), se o estado está nos estados adequados, etc...
                            if(carro_preco <= 0 or carro_ano <= 0):
                                os.system("cls")
                                temporaryMessage("Você digitou um valor errado", 1.5)
                                continue
                                
                            cadastrar_carros(carro_nome, carro_preco, carro_ano, carro_estado)
                                
                        except ValueError:
                            print("Digite apenas os valores adequados")
                            time.sleep(1)
                            continue

                case 2:
                    print("👋 Saindo do programa...")
                    break

                case _:
                    temporaryMessage("Digite um dos valores fornecidos", 1.5)
                    number = menu_principal()
                    continue
  
            deseja_continuar = input("Deseja continuar? (sim / não): ").lower()
            
            if(deseja_continuar == "não" or deseja_continuar == "n"):
                os.system("cls")
                break
            elif(deseja_continuar == "sim" or deseja_continuar == "s"):
                continue
            else:
                temporaryMessage("Essa não é uma opção válida", 1)

    except:
        print("⚠️ Algo deu errado... Voltando ao menu principal.")    

main()
