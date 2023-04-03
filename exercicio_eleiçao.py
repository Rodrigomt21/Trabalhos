joao = 0
jose = 0
maria = 0
joana = 0
nulo = 0
branco = 0
for cont in range(1,101):
    f = False
    while not f:
        try:
            qual = float(input("1= JOAO\t2=JOSE\t3=MARIA\t4=JOANA\t0=BRANCO\tRESTO NULO\t-1=FIM: "))
            f = True
        except:
            print("ERRO, DIGITE UM numero plausivel")
    if qual == 1:
        check = float(input("voce deseja mesmo votar no joao?(1=Sim, 2+Nao)?"))
        if check == 1:
            joao += 1
    elif qual == 2:
        check = float(input("voce deseja mesmo votar no jose?(1=Sim, 2+Nao)?"))
        if check == 1:
            jose += 1
    elif qual == 3:
        check = float(input("voce deseja mesmo votar na Maria?(1=Sim, 2+Nao)?"))
        if check == 1:
            maria += 1
    elif qual == 4:
        check = float(input("voce deseja mesmo votar na joana?(1=Sim, 2+Nao)?"))
        if check == 1:
            joana += 1
    elif qual == 0:
        check = float(input("voce deseja mesmo votar em Branco?(1=Sim, 2+Nao)?"))
        if check == 1: 
            branco += 1
    elif qual == (5 or 6 or 7 or 8 or 9):
        check = float(input("voce deseja mesmo votar nulo?(1=Sim, 2+Nao)?"))
        if check == 1:
            nulo += 1
    elif qual == -1:
        break

total = joao + maria + jose + joana + branco + nulo
nulos = (nulo / total) / 100
brancos = (branco / total) / 100
print(f"Joao recebeu:{joao}\nJose recebeu:{jose}\nMaria recebeu:{maria}\nJoana recebeu:{joana}")
print(f"{nulo} votos nulos")
print(f"{branco} votos em branco")
print(f"{nulos} é a porcentagem de nulos")
print(f"{brancos} é a porcentagem de votos em branco")


    

    
    