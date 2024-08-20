import argparse

def add(num1, num2):
    print(f"addition value of {num1} {num2} is {int(num1)+int(num2)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Addition program"
    )

    parser.add_argument(
        "-n1", "--num1", required=True, 
        )

    parser.add_argument(
        "-n2", "--num2", required=True
        )

    args= parser.parse_args()

    add(args.num1, args.num2)