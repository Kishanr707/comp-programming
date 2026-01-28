def binomial_coefficient(n, k):
    if k > n or k < 0:
        raise ValueError(f"Invalid input: k ({k}) must be between 0 and n ({n})")
    if k == 0 or k == n:
        return 1
    
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result

try:
    k, r = map(int, input("Enter k and r: ").split())

    numerator = binomial_coefficient(13, r) * binomial_coefficient(39, k - r)
    denominator = binomial_coefficient(52, k)

    probability = numerator / denominator

    if probability == 0:
        raise ValueError("Probability is 0: this event is impossible")

    print(f"Probability: {probability:.6f}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError:
    print("Error: Division by zero occurred")
