print("Welcome to the MULTIPLICATION TABLE GENERATOR\n")
number = int(input("Enter a number to get its multiplication table: "))
limit = int(input("Enter its limit(where to stop): "))

print(f"Multiplication table for {number}")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}\n")

print("Welcome to the DIVISION TABLE GENERATOR\n")
number = int(input("Enter a number to get its division table: "))
limit = int(input("Enter its limit(where to stop): "))

print(f"Division table for {number}")
for i in range(1, limit + 1):
    print(f"{i} / {number} = {round(i / number, 2)}\n")
