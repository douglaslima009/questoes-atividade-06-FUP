vetor = []
for i in range(4):
    valor = int(input(f"Digite um valor: "))
    vetor.append(valor)

i = 0
while i < len(vetor):
    if vetor[i] == 0:
        vetor.pop(i)
    else:
        i += 1

print("Vetor compacto:")
for valor in vetor:
    print(valor, end=" ")