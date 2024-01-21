import sys

def get_factor(num):
    if num <= 1:
        print(f"{num} is not factorizable.")
        return
    for i in range(2, num):
        if num % i == 0:
            a = num // i
            print(f"{num}={a}*{i}")
            return
def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                num = int(line.strip())
                get_factor(num)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except ValueError:
        print(f"Invalid data in file '{file_name}'.")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    # Extract filename from command-line arguments
    file_name = sys.argv[1]

    # Process the file and print factorizations
    process_file(file_name)
