import sys

def main():

    x = int(10)
    x += 5
    print(f"={x}")
    x -= 5
    print(f"={x}")
    x *= 5
    print(f"={x}")
    x **= 5
    print(f"={x}")

if __name__ == "__main__":
    sys.exit(main())