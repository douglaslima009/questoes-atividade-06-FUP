numbers = []

for i in range(10):
    valor = float(input("Digite um valor: "))
    numbers.append(valor)
    quadrados = [x**2 for x in numbers]

print("O conjunto dos números originais, antes da transformação em quadrados é: ")
for num in numbers:
    print(num, end=" ")

print("O conjunto dos números originais, antes da transformação em quadrados é: ")
for quad in quadrados:
    print(quad, end=" ")