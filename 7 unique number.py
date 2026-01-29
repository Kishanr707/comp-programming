import sys
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
if len(arr) != n:
    print("Error: Number of elements doesn't match n", file=sys.stderr)
    exit(1)
result = 0
for num in arr:
    result ^= num
print(f"Unique number is {result}")