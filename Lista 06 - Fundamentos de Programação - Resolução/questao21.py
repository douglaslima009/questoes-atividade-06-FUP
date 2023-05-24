vetor = []
primos = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    vetor.append(num)

for i in range(len(vetor)):
    primoreal = True
    if vetor[i] < 2:
        primoreal = False
    else:
        for j in range(2, vetor[i]):
            if vetor[i] % j == 0:
                primoreal = False
                break
    if primoreal:
        primos.append((vetor[i], i))

print("Os números primos encontrados no vetor são:")
for primo, position in primos:
    print(f"Número primo: {primo} na posição: {position}")
