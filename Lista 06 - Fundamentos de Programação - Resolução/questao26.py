vetor = []
for i in range(15):
    numero = float(input("Digite um número real: "))
    vetor.append(numero)

for i in range(len(vetor)):

    for j in range(i+1, len(vetor)):
        if vetor[i] < vetor[j]:
            vetor[i], vetor[j] = vetor[j], vetor[i]

print("Vetor ordenado:")
for numero in vetor:
    print(numero)