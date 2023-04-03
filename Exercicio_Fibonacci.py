check = False
while not check:
    try:
        quantidade = int(input("Quantas vezes voce deseja que ocorra?: "))
        check = True
    except:
        print("ERRO: DIGITE UM NUMERO INTEIRO")

num1 = 1
num2 = 1
for cont in range(1, quantidade + 1):
    proximon = num1 + num2
    num1 = num2
    num2 = proximon
    print(proximon)

        
            
    
