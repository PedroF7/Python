number = input("Digite um número: ")

try:
    result = int(number**number)
except:
    print('Nao deu pra abrir o arquivo')
else:
    print(result)

print(5**2)