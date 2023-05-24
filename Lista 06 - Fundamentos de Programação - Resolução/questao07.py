vetor = []
impares = 0

for i in range(15):
    valor = int(input(f'Digite um valor: '))
    vetor.append(valor)
    if valor % 2 == 1:
        impares += 1
print(f"O vetor possui {impares} valor(es) ímpar(es).")