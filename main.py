prod1 = input("Digite o nome do primeiro produto: ")
quant1 = int(input("Digite a quantidade do primeiro produto: "))
valor1 = float(input("Digite o valor do primeiro produto: "))
prod2 = input("Digite o nome do segundo produto: ")
quant2 = int(input("Digite a quantidade do segundo produto: "))
valor2 = float(input("Digite o valor do segundo produto: "))
print(f'{"Produto":20}|{"Quantidade":^12}|{"Valor":>10}')
print(f'{prod1:20}|{quant1:^12}|{valor1:10.2f}')
print(f'{prod2:20}|{quant2:^12}|{valor2:10.2f}')