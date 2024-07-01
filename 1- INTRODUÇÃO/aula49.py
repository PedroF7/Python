n = (input("Digite um número: "))

try: #Código que será rodado
    result = int(n)**int(n)
except:  #O que será feito caso seja um erro
    print("Não é um number")
else: #Caso não seja um erro
    print(f"O número que vc digitou '{n}' e ele elevado a {n} é igual a: {result}")
finally: #Será feito independente das circunstancias 
    print(f"vc digitou '{n}'")