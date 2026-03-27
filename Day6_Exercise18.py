import sys

def main():

    number = input("Kindly input a number: ")
    number = int(number) #Variable converted to an integer
    print(f"{number}")

    number = None #Variables are dynamically typed, can hold any type at any time.
    print(f"{number}")




if __name__ == "__main__":
    sys.exit(main())