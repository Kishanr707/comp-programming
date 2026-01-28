n, m = map(int, input("Enter no. of elements and modulo: ").split())
arr = list(map(int, input("Enter list elements: ").split()))
result  = 0
for i in arr:
    result = (result + (i%m))%m
print(result)