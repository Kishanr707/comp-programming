import sys
def main():
    try:
        n = int(input("Enter the number of packets: "))
    except Exception:
        return
    try:
        arr = list(map(int, input("Enter the packet values: ").split()))
    except Exception:
        arr = []
    if len(arr) < n:
        remaining = []
        for _ in range(n - len(arr)):
            try:
                remaining.append(int(input()))
            except Exception:
                break
        arr.extend(remaining)
    try:
        checksum = int(input("Enter the expected checksum: "))
    except Exception:
        print("ANOMALY")
        return

    xor = 0
    for x in arr[:n]:
        xor ^= x

    if xor == checksum:
        print("OK")
    else:
        print("ANOMALY")


if __name__ == '__main__':
    main()
