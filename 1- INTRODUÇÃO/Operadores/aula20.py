primer_value = input("Digite um valor: ")
second_value = input("Digite outro valor: ")

if primer_value > second_value:
    print(f"{primer_value} é maior que {second_value}")
elif second_value > primer_value:
    print(f"{second_value} é maior que {primer_value}")
else:
    print("erro ao indentificar um número")