from collections import defaultdict
vetor = []

for i in range(10):
    valor = float(input(f'Digite um valor: '))
    vetor.append(valor)

for i, num in enumerate(vetor):
    if num in vetor[i+1:]:
        print(f"O elemento {num} está sendo repetido.")