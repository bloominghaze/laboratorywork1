n = 20
product = 1
sum_of_elements = 0

for i in range(1, 2*n, 2):
    product *= i
    sum_of_elements += i

print(f"Сума елементів ряду: {sum_of_elements}")
print(f"Добуток елементів ряду: {product}")
