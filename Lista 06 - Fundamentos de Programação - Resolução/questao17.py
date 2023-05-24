vetor1 = []
for i in range(10):
    num = int(input("Vetor 1 -> Digite um número inteiro: "))
    vetor1.append(num)

vetor2 = []
print("\n")
for i in range(10):
    num = int(input("Vetor 2 -> Digite um número inteiro: "))
    vetor2.append(num)

vetor3 = []
for i in range(10):
    if i % 2 == 0:
        vetor3.append(vetor1[i])
    else:
        vetor3.append(vetor2[i])

print(f"O vetor formado com os valores pares e ímpares é:")
for valor in vetor3:
    print(valor, end=" ")