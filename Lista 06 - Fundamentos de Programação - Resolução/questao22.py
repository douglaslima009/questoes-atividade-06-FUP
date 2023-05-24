vetor1 = []
for i in range(15):
    elemento = int(input("Vetor 1 -> Digite um valor: "))
    vetor1.append(elemento)

vetor2 = []
for i in range(15):
    elemento = int(input("Vetor 2 -> Digite um valor: "))
    vetor2.append(elemento)

vetor3 = []
for elemento in vetor1:
    if elemento in vetor2 and elemento not in vetor3:
        vetor3.append(elemento)

print(f"O vetor de interseção é formado da seguinte forma: {vetor3}")
