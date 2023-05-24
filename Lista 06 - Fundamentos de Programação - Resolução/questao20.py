vetor = []
num = 1
while len(vetor) < 100:
    if num % 7 != 0 and num % 10 != 7:
        vetor.append(num)
    num += 1
print(vetor)