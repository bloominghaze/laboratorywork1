def input_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= 100:
                return number
            else:
                print("Помилка! Число повинно бути в діапазоні від 1 до 100.")
        except ValueError:
            print("Помилка! Введіть ціле число.")

a = input_number("Введіть значення a (від 1 до 100): ")
b = input_number("Введіть значення b (від 1 до 100): ")

if a > b:
    X = a / b + 1
elif a == b:
    X = a + 25
else:
    X = (a * b - 2) / a

print(f"Значення X: {X}")
