vetor = []
for i in range(20):
    valor = float(input(f'Digite um valor: '))
    vetor.append(valor)
vetorsemrepetir = []
for num in vetor:
    if num not in vetorsemrepetir:
        vetorsemrepetir.append(num)
        vetorsemrepetir.sort()
print(f"Vetor sem elementos repetidos: {vetorsemrepetir}")  