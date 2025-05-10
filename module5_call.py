from module5_mod import Numbers

def main():
    n = int(input("Enter a positive integer: "))
    num_list= Numbers()
    num_list.add_number(n)
    x = int(input("Enter a number to search for: "))
    result = num_list.find_number(x)

    if result == -1:
        print("-1")
    else:
        print(f"The number {x} was found at position {result}")

if __name__ == "__main__":
    main()