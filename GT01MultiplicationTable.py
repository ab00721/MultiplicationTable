mystery_int = 5
table = "Multiplication table:"
print (table)
for i in range(1, mystery_int + 1):
    row = ""
    for j in range(1, mystery_int + 1):
        product = i * j
        row += str(product) + "\t"
    print(row)