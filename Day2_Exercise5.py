import sys

def main():

    x = int(input("Kindly input the value of x = "))
    y = int(input("Kindly input the value of y = "))

    print(f"The quotient = {x / y}")
    print(f"The integer division = {x // y}")
    print(f"The reminder = {x % y}")

if __name__ == "__main__":
    sys.exit(main())