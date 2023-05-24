vetor = []
while len(vetor) < 12:
    numero = int(input("Digite um número: "))
    if numero in vetor:
        print("Esse número já foi digitado. Digite outro número.")
    else:
        vetor.append(numero)
print("Vetor final:", vetor)
