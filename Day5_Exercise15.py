import sys

def main():

    fruit = str(input("What is your favourite fruit: "))
    start_with_a = fruit[0].lower() == 'a'
    if start_with_a:
        print(f"True")
    else:
        print(f"False")


if __name__ == "__main__":
    sys.exit(main())