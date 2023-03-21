radicando = float(input("Extrair raiz quadrada de: "))
CasasDec = int(input("Qual a precisao desejada(casas decimais?) "))
precisao = 10 ** (-CasasDec)
tentativas = 0
low = 0
high = max(1, radicando)
raiz = (low + high)/2
while abs(raiz ** 2 - radicando) >= precisao:
    #print(f"low = {low:10.10f} \t high = {high:10.10f}")
    tentativas += 1
    if raiz ** 2 < radicando:
        low = raiz
    else:
        high = raiz
    raiz = (low + high)/2
print(f'''\nA raiz quadrada de {radicando} é {raiz:.{CasasDec}f}, 
dentro da precisao de {CasasDec},
 casas decimais.Foram necesarias {tentativas} tentativas''')