#!/usr/bin/python3
import sys

def factorize(num):
    for i in range(2, num):
        if num % i == 0:
            return (i, num // i)

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                num = int(line.strip())
                factors = factorize(num)
                if factors:
                    p, q = factors
                    print(f"{num}={p}*{q}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
