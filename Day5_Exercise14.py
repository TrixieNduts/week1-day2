import sys

def main():

    a = float(input("Kindly input the value of a: "))
    b = float(input("Kindly input the value of b: "))

    print(f"={a > b}")
    print(f"={a == b}")
    print(f"={a != b}")


if __name__ == "__main__":
    sys.exit(main())