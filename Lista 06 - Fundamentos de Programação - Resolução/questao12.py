vetor = []

for i in range(12):
    valor = float(input(f'Digite um valor: '))
    vetor.append(valor)

quantnegativos = 0
for num in vetor:
    if num < 0:
        quantnegativos += 1

print(f"A quantidade de números negativos nesse vetor é de: {quantnegativos}")
print(f"A soma dos valores positivos do vetor é igual a: {sum(filter(lambda x: x > 0, vetor))}")