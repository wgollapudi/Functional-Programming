def fibonacci(n):
    if (n <= 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    for num in range(15):
        print(f"{num} - {fibonacci(num)}")

if __name__ == '__main__':
    main()