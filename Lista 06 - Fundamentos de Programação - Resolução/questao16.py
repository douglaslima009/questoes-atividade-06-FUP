vetora = []
for i in range(10):
    num = int(input("Vetor A -> Digite um número inteiro: "))
    vetora.append(num)

vetorb = []
print("\n")
for i in range(10):
    num = int(input("Vetor B -> Digite um número inteiro: "))
    vetorb.append(num)

vetorc = []
for i in range(10):
    diferenca = vetora[i] - vetorb[i]
    vetorc.append(diferenca)

print("\nO vetor C, que é a diferença entre A e B, é:")
for num in vetorc:
    print(num, end=" ")
print()