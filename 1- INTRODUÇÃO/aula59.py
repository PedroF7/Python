tst = True
while tst:
    try:
        np = input('Digite um número: ')
        if float(np) < 0:
            print(f"'{np}' é negativo")
            print("Encerrando o programa...")
            break
        else:
            print(f"'{np}' + '{np}' é igual a: {float(np)+float(np) :.1f}")
    except:
        print(f'"{np}" não é um número')
        print("tenta novamente")
    

n = 0
while n<=10:
    print(n)
    n+=1