from statistics import mean
vetor = []

for i in range(30):
    valor = int(input(f'Digite uma nota: '))
    vetor.append(valor)

print(f"A média aritmética dos valores digitados é: {mean(vetor)}")
for valor in vetor:
    if valor < 6:
        print(f"A seguinte nota está abaixo da média: {valor}")
