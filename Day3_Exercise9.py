import sys

def main():

    message = str(input("Kindly input a short message about your life: "))

    print(f"{message * 3}.")


if __name__ == "__main__":
    sys.exit(main())