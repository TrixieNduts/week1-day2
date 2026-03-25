import sys

def main():

    number = int(input("Kindly input an integer = "))

    print(f" The int = {number}.")
    print(f" The float = {number.__float__()}.")



if __name__ == "__main__":
    sys.exit(main())