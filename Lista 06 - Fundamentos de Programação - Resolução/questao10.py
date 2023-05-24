from statistics import mean
vetor = []
impares = 0

for i in range(15):
    valor = int(input(f'Digite um valor: '))
    vetor.append(valor)

print(f"A média aritimética dos valores digitdos é: {mean(vetor)}")