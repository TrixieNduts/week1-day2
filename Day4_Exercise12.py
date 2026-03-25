import sys

def main():

    word = str(input("Kindly input a word: "))
    number = int(input("Kindly input a number: "))

    print(f"{word  * number}.")

if __name__ == "__main__":
    sys.exit(main())