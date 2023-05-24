vetor = []
for i in range(70):
    valor = (i + 5 * i) % (i + 1)
    vetor.append(valor)
for elemento in vetor:
    print(elemento)

