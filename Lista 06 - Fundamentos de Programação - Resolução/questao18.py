vetor = []
for i in range(100):
    valor = float(input(f"Digite um valor: "))
    vetor.append(valor)

while True:
    opcoes = int(input("\nDigite o código (0 para sair, 1 para mostrar o vetor direto, 2 para mostrar o vetor invertido): "))

    if opcoes == 0:
        print("Encerrado.")
        break
    elif opcoes == 1:
        print("O vetor na ordem direta: ")
        for valor in vetor:
            print(valor)
    elif opcoes == 2:
        print("o vetor na ordem inversa:")
        for valor in reversed(vetor):
            print(valor)
    else:
        print("Digite uma opção válida.")