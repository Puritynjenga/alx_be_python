length = int(input("Enter the size of the pattern: "))
 
row = 0
while row < length:
    col = 0
    for col in range(1, length +1):
          print("*", end="")
          col += 1
    print()  
    row +=1    


