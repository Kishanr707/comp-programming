try:
    n, k = map(int, input("Enter number of employees " \
            "and teams to be formed: ").split())
    if k < 0 or k > n:
        result = 0
    elif k == 0 or k == n:
        result = 1
    else:
        if k > n // 2:
            k = n - k
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
            
    print(f"Number of teams that can be formed is {result}")
except ValueError:
    print("Enter valid numbers")
