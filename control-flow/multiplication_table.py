number = int(input("Enter a number to see its multiplication table: ")) 
for num in range(1, 11):
    #print(num)
    product = num * number
    print(f"{number} * {num} = {product}")

