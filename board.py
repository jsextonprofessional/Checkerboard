def board(x, y):
    result = []

    for a in range(0, y):
        output = []
        for b in range(0, x):
            output.append((a + b) % 2)
        result.append(output)

    return result

result = board(8,9)

for row in result:
    print(row)