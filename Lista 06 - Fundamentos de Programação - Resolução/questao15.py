vetor = []
for i in range(10):
    valor = int(input(f'Digite um valor: '))
    vetor.append(valor)
x = int(input("Digite um número inteiro x: "))

multiplos = []
for numero in vetor:
    if numero % x == 0:
        multiplos.append(numero)
print(f"Os múltiplos de {x} no vetor são: {multiplos}")
