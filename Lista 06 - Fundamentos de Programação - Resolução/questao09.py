vetor = []
for i in range(20):
    valor = int(input(f'Digite um valor: '))
    if valor < 0:
        valor = 0
    vetor.append(valor)
print(f"Após a operação de atribuição, o vetor ficou desta forma: {vetor}")