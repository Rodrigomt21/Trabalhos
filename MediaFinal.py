pesos = [0.3, 0.3, 0.2, 0.2]
notas = []
print("***notas de prova***")
for contador in range(2):
    NotaOk = False
    while not NotaOk:
        nota = float(input(f"Digite a nota da p{contador + 1}: "))
        if(0 <= nota <=10):
            notas.append(nota)
            NotaOk = True
        else:
            print("ERRO Digite um numero entre 0 e 10")
print("***notas de trabalho***")
for contador in range(4):
    NotaOk = False
    while not NotaOk:
        nota = float(input(f"Digite a nota da T{contador + 1}: "))
        if(0 <= nota <=10):
            notas.append(nota)
            NotaOk = True
        else:
            print("ERRO Digite um numero entre 0 e 10")
#Calculo da media final
mult = []
for contador in range(len(notas)):
    mult.append(pesos[contador] * notas[contador])
MF = sum(mult)
print(f"\nMedia Final = {MF:.1f}")    

