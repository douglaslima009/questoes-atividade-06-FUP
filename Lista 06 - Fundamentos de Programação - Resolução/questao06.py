vetor = []
pares = 0

for i in range(15):
    valor = int(input(f'Digite um valor: '))
    vetor.append(valor)
    if valor % 2 == 0:
        pares += 1
print(f"O vetor possui {pares} valor(es) par(es).")