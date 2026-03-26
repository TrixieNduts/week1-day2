from selectors import SelectSelector

import sys

def main():

    age = int(input("Kindly input your age: "))
    if age >= 18:
     print(f"Welcome to the program.")
    else:
        print(f"Sorry,the minimum age entry is 18!")

if __name__ == "__main__":
    sys.exit(main())