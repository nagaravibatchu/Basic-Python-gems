## Different arthmetic operations

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
art_opr = int(input("Enter the arthametic operation you want:" \
"Choose from the following:" \
"1.Sum" \
"2.Difference" \
"3. Product" \
"4. Division" \
"5. Floor Division" \
"6. Modulus" \
"7. Exponential" \
"8. All"))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2
floor = num1 // num2
modulus = num1 % num2
exp = num1 ** num2

if art_opr==1:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Sum of 2 numbers:", sum)
elif art_opr==2:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Difference of 2 numbers:", diff)
elif art_opr==3:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Multipliation of 2 numbers:", prod)
elif art_opr==4:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Division of 2 numbers:", div)
elif art_opr==5:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Floor division of 2 numbers:", floor)
elif art_opr==6:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Modulus of 2 numbers:", modulus)
elif art_opr==7:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Exponential of 2 numbers:", exp)
elif art_opr==8:
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Results of all operations:") 
    print("\n", "Sum:", sum, "\n", "Difference:", diff, "\n", "Multiplication:", prod, "\n", "Division:", div, "\n",
     "Floor Division:", floor, "\n", "Modulus:", modulus, "\n", "Exponential:", exp)