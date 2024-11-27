import os
import time

fileName = "carros_cadastrados.txt"

def createFile():
    # Check if the file already exists, if no create a new one with the pionner cars.
    try:
        with open(fileName) as file:
            file.read()
    except FileNotFoundError:
        registerPioneerCars()

def registerPioneerCars():
    # Create the file and regist the first cars.
    firstCars = [
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

    for car in firstCars:
        with open(fileName, "a", encoding = "utf-8") as file:
            file.write(str(f"{car['nome']}, {car['preco']}, {car['ano']}, {car['estado']} \n"))

def temporaryMessage(message: str, timer: float):
    # Print a message and stop the runtime of the code by a certain time.
    print(message)
    time.sleep(timer)

def returnDictOfFile():
    # Get the data in the txt file, and convert it in a dict.
    registedCars = []

    with open(fileName, "r") as file:
        for line in file:
            # For each line, he get the elements in that line, split and strip them,
            # save them as a dict in a local variable, and append this variable to a array of dict
            line = line.strip()
            lineElements = line.split(",")
            car = {'nome': lineElements[0], 'preco': float(lineElements[1]), 'ano': int(lineElements[2]), 'estado': lineElements[3].strip()}
            registedCars.append(car)
            
    return registedCars

def findCars(whatToFind):
    # We get what the user wants to find(max price, name, etc...) and filter the cars based on that information.
    cars = returnDictOfFile()

    while True:
        
        os.system("cls")

        # match the thing the user wants to find the car based on and look for that.
        match whatToFind.lower():
            case "nome":
                name = input("📛 Digite o nome completo do carro: ").lower()
                filteredCars = [car for car in cars if name in car['nome'].lower()]
                break
            case "ano":
                year = int(input("🗓️ Digite o ano do carro: "))
                filteredCars = [car for car in cars if car['ano'] == year]
                break
            case "preco":
                maxPrice = float(input("💵 Digite o preço máximo: "))
                filteredCars = [car for car in cars if car['preco'] <= maxPrice]
                break
            case "estado":
                status = input("📋 Digite o estado do carro (novo, seminovo, conservado, mal estado): ").lower()
                filteredCars = [car for car in cars if car['estado'] == status]
                break
            case _:
                temporaryMessage("Por favor, digite um valor válido", 1.5)

    temporaryMessage("Carregando os carros disponíveis...", 1)

    return filteredCars

def findCarsMenu(): 
    # Print the options that the user have in the find cars menu, and get the user option based on that.
    os.system("cls")

    while True:
        try:
            print("================ Buscar Carros ================")
            print("[1] - 📛 Buscar por Nome")
            print("[2] - 🗓️ Buscar por Ano")
            print("[3] - 💵 Buscar por Preço maximo")
            print("[4] - 📋 Buscar por Estado")
            print("[0] - 🔙 Voltar ao Menu Principal")
            print("===============================================")
            option = int(input("Escolha uma opção de busca: "))

            match option:
                case 0:
                    return
                case 1:
                    suitableCars = findCars("Nome")
                case 2:
                    suitableCars = findCars("Ano")
                case 3:
                    suitableCars = findCars("Preco")
                case 4:
                    suitableCars = findCars("Estado")
                case _:
                    temporaryMessage("⚠️ Por favor, use apenas numeros validos", 1.5)
                    os.system('cls')
                    continue
            if(type(suitableCars) != None): 
                return suitableCars

        except ValueError:
            temporaryMessage("⚠️ Opa, parece que você digitou um valor errado. Tente novamente utilizando os valores certos.", 1.5)
            os.system('cls')

def registCars(name: str, price: float, year: int, status: str):
    # Get the information from the user and regist his car.
    car = {'nome': name, 'preco': price, 'ano': year, 'estado': status}

    with open(fileName, "a", encoding = "utf-8") as file:
        file.write(str(f"{car['nome']}, {car['preco']}, {car['ano']}, {car['estado']} \n"))

    print("✅ Carro cadastrado com sucesso!")

def printCarDisponible(suitableCars):
    # Prints the result of the search of cars.
    os.system("cls")

    if (len(suitableCars) == 0):
        print("Não há carros adequados")
        
    else:
        os.system("cls")
        for car in suitableCars:
            print(f"🏷️  Carro: {car['nome']} \n  💲 Preço: {car['preco']} \n  🗓️  Ano: {car['ano']} \n  🚨 Estado: {car['estado']} \n")

def mainMenu():
    # Print the main menu and give options to the user to choose from.
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
            temporaryMessage("⚠️ Por favor, use apenas números", 1.5)
            os.system('cls')
    
def main():
    # The main part of the code
    try:
        createFile()

        number = mainMenu()

        while True:
            
            match number:
                case 0:
                    # Find cars system

                    cars = findCarsMenu()
                    if(cars != None):
                        printCarDisponible(cars)
                    else:
                        number = mainMenu()
                        continue
                
                case 1:
                    #  Regist cars system
                    os.system("cls")
                    try:
                        # Get the user's car information
                        carName = input("Qual o nome do carro: ")
                        carPrice = float(input("Qual o preço do carro: "))
                        carYear = int(input("Qual o ano do carro: "))
                        carStatus = input("Qual o estado atual do carro (novo, seminovo, conservado, mal estado): ").lower()

                        # Check if the price and the year is valid.
                        if(carPrice <= 0 or carYear <= 0):
                            os.system("cls")
                            temporaryMessage("Você digitou um valor errado", 1.5)
                            continue
                            
                        registCars(carName, carPrice, carYear, carStatus)
                            
                    except ValueError:
                        print("Digite apenas os valores adequados")
                        time.sleep(1)
                        continue
                
                case 2:
                    os.system('cls')
                    temporaryMessage("👋 Saindo do programa...", 1)
                    break

                case _:
                    temporaryMessage("Digite um dos valores fornecidos", 1.5)
                    number = mainMenu()
                    continue
  
            wantToContinue = input("Deseja continuar? (sim / não): ").lower()
            
            if(wantToContinue == "não" or wantToContinue == "n"):
                os.system("cls")
                break
            elif(wantToContinue == "sim" or wantToContinue == "s"):
                continue
            else:
                temporaryMessage("Essa não é uma opção válida \nSaindo do programa...", 2)
                os.system('cls')
                return

    except:
        print("⚠️ Algo deu errado... Voltando ao menu principal.")    

main()