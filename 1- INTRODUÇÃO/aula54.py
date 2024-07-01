n = input("Digite um número inteiro:")
try:
    teste = int(n) % 2
except:
    print(f"{n} não é um número inteiro")
else:
    print("é par") if teste == 0 else print("é impar")
finally:
    print(f"você digitou '{n}'")

from datetime import datetime
print(f'{datetime.now().hour}:{datetime.now().minute}')

now = datetime.now().hour
if now <= 4:
    print("Boa madrugada")
elif now <= 12:
    print("Bom dia")
elif now <= 17:
    print("Boa tarde")

name = input("Digite seu nome: ")
if len(name) <= 4:
    print("Nome curto")
elif len(name) == 5 or len(name) == 6:
    print("normal")
else:
    print("grande")