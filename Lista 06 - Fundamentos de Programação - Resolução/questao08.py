vetor = []

for i in range(10):
    valor = int(input(f'Digite um valor: '))
    vetor.append(valor)

maiorvalor = vetor[0]
menorvalor = vetor[0]

for valor in vetor:
    if valor > maiorvalor: 
        maiorvalor = valor
    if valor < menorvalor:
        menorvalor = valor

print(f"O maior valor descrito na lista é: {maiorvalor}")
print(f"O menor valor descrito na lista é: {menorvalor}")