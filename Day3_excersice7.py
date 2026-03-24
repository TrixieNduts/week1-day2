import sys

def main():

    word = str(input("kindly input your favourite word, "))
    first_char = word[0]
    second_char = word[1]

    print(f"First character = {first_char}")
    print(f"First character = {second_char}")

if __name__ == "__main__":
    sys.exit(main())