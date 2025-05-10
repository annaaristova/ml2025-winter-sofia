class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        for i in range(n):
            num = int(input(f"Enter a number: "))
            self.numbers.append(num)

    def find_number(self, x):
        if x in self.numbers :
            index = self.numbers.index(x) + 1
            return index
        else:
            return -1


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