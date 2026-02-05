n = int(input("Enter number of finshing times: "))
arr = list(map(int, input("Enter the finishing times: ").split()))
if len(arr) != n:
    print("Error: Number of finishing times doesn't match n")
    exit(1)
result = 0
print(f"The finishing times are: {arr}")