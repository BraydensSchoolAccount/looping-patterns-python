# Looping patterns
# Brayden Towner
# 02/28/2024

# Do this 4 times
for i in range(1, 5):
    # It prints the number 'i' 5-i times
    # So if i=1, print(1) 5-1 times. i=2, print(i) 5-2 times, so on and so forth
    for j in range(5 - i, 0, -1):
        print(i, end="\t")
    print()

print("---------------------------------------------------")
# Do this 5 times
for i in range(1, 6):
    # i is how many numbers are printed
    # This essentially counts up and prints it
    for j in range(1, i + 1):
        print(j, end="\t")
    print()
print("---------------------------------------------------")

# Odd numbers descending
for i in range(9, 0, -2):
    # i // 2 checks how many times it needs to print
    # 9 / 2 = 4.5 floored is 4, +1 is 5
    # 7 / 2 = 3.5 floored is 3, +1 is 4, yada yada
    for j in range(1 + (i // 2), 0, -1):
        print(i, end="\t")
    print()
print("---------------------------------------------------")

# does it 8 times
for i in range(4, -5, -1):
    # Determines how many times it prints
    # For positive numbers, it starts at 5-4, printing 1 time
    # Once it reaches 0 (5-0), it subtracts the absolute number and goes back down
    # 5-abs(-1) = 5-1
    for j in range(5 - abs(i)):
        print("*", end="\t")
    print()
