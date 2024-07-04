while True:
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    opr = input("Digite um operador(-/*+): ")
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    oprChecked = '/*+-'
    if numeros_validos is None:
        print("Um ou ambos números digitados são inválidos..")
        break
    elif opr not in oprChecked:
        print(f"Você não pode usar {opr} de operador")
        break
    elif len(n1) > 1 or len(n2) > 1:
        print("Digite apenas um número")
        break
    print(n1_float + n2_float) if opr == '+'  else ''
    print(n1_float - n2_float) if opr == '-'  else ''
    print(n1_float * n2_float) if opr == '*'  else ''
    print(n1_float / n2_float) if opr == '/'  else ''
    
    confirm = input("Quer sair? [s] Sim ou [n] Não?")     
    if confirm == 's' or confirm =='S':
        break
    elif confirm == 'n' or confirm =='N':
        continue

    if confirm != 'S' or confirm != 's' or confirm != 'n' or confirm == 'N':
        print(f"Você digitou '{confirm}'")
        print("Vou entender como um não..")
        break