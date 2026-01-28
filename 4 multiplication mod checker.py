a, b, p = map(int, input("Enter a, b and modulo values: ").split())
k = int(input("Enter integer to divide with: "))
result = ((a%p)*(b%p))%p
if result%k == 0:
    print("Divisible")
else:
    print("Not divisible")