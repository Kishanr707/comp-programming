def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

n = int(input("Enter number of finshing times: "))
arr = list(map(int, input("Enter the finishing times: ").split()))
if len(arr) != n:
    print("Error: Number of finishing times doesn't match n")
    exit(1)

print(f"The finishing times are: {arr}")

# Sort in ascending order
quick_sort(arr)
print(f"Sorted finishing times: {arr}")

# Print the third number
if len(arr) >= 3:
    print(f"The third number: {arr[2]}")
else:
    print("Array has less than 3 elements")
