def print_pattern(N):

    for i in range(1, N + 1):
        print("  " * (N - i), end="")
        for j in range(N, N - i, -1):
            print(j, end=" ")
        print()

    for i in range(1, N + 1):
        print("  " * (N - 1), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

while True:
    N = int(input("Введіть ціле число N (1 < N < 9): "))
    if 1 < N < 9:
        break
    else:
        print("Помилка: число повинно бути в діапазоні від 2 до 8. Спробуйте знову.")

print_pattern(N)
