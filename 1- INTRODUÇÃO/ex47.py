name = input("Digite seu nome:")
age = input("Digite sua idade:")

if name or age:
    print(
        f'Seu nome é: {name}\n'
        f'Seu nome invertido é: {name[::-1]}\n'
        "tem espaço"if ' ' in name else 'nao tem espaço'
        f'Seu nome tem {len(name)} letras \n'
        f'A primeira letra do seu nome é: {name[0:1]}\n'
        f'A última letra do seu nome é {name[-1::]}\n'
    )
else:
    print("Você nao digitou nada")