# Leitura dos vetores
vetor1 = []
for i in range(4):
    elemento = int(input("Vetor 1 -> Digite um valor: "))
    vetor1.append(elemento)

vetor2=[]
for i in range(4):
    elemento = int(input("Vetor 2 -> Digite um valor: "))
    vetor2.append(elemento)

vetor3 = vetor1.copy()

for elemento in vetor2:
    if elemento not in vetor3:
        vetor3.append(elemento)

print("O vetor da união dos elementos dos vetores 1 e 2 é formado por: ")
for elemento in vetor3:
    print(elemento)
