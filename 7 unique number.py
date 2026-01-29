n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

result = 0
for num in arr:
    result ^= num
print(f"Unique number is {result}")