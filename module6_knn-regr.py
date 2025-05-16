import numpy as np 

class NearestNeighbor:
    def __init__(self):
        self.x_numbers = []
        self.y_numbers = []
    
    def add_x_y(self, n):
        print(f"Enter {n} (x, y) points:")

        for i in range(n):
            x = float(input(f"Point {i+1} for x: "))
            y = float(input(f"Point {i+1} for y: "))
            self.x_numbers.append(x)
            self.y_numbers.append(y)
    
    def find_distance(self, x, k):
        x_numbers = np.array(self.x_numbers)
        y_numbers = np.array(self.y_numbers)

        distance = np.sqrt((x_numbers - x)**2) 
        indices = np.argsort(distance)[:k]
        nearest_y = y_numbers[indices]
        y = np.mean(nearest_y)
        print(f"Using {k}-NN Regression, the predicted Y for X = {x} is: {y}")


def main():
    n = int(input("Enter a positive integer N: "))
    k = int(input("Enter a positive integer k: "))

    if k > n:
        print("Error: k cannot be greater than N")
        exit()

    nearest_neighbor = NearestNeighbor()
    nearest_neighbor.add_x_y(n)

    x = float(input("Enter query X: "))
    nearest_neighbor.find_distance(x, k)

if __name__ == "__main__":
    main()