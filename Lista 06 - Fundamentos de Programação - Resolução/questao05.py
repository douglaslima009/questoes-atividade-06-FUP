numbers = []

for i in range(15):
    valor = int(input("Digite um valor para a posição {}: ".format(i)))
    numbers.append(valor)

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if x >= 0 and x < 15 and y >= 0 and y < 15:
    soma = numbers[x] + numbers[y]
    print("A soma dos valores nas posições {} e {} é: {}".format(x, y, soma))
else:
    print("Valores de X e Y inválidos. As posições devem estar entre 0 e 14.")