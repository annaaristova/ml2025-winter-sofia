import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class NearestNeighbor:
    def __init__(self, n):
        self.n = n
        self.x_numbers = np.empty(n)
        self.y_numbers = np.empty(n)

    def fit(self):
        print(f"Enter {self.n} (x, y) points:")
        for i in range(self.n):
            x = float(input(f"  Point {i+1} for x: "))
            y = float(input(f"  Point {i+1} for y: "))
            self.x_numbers[i] = x
            self.y_numbers[i] = y
    
    def predict(self, x, k):
        variance = np.var(self.y_numbers)
        print(f"Variance of Y values: {variance}")

        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(self.x_numbers.reshape(-1, 1), self.y_numbers)

        x_query = np.array([[x]]) 
        predicted_y = knn.predict(x_query)[0]

        print(f"Using {k}-NN Regression, the predicted Y for X = {x} is: {predicted_y}")

def main():
    n = int(input("Enter a positive integer N: "))
    if n <= 0:
        print("N must be a positive integer.")
        return

    k = int(input("Enter a positive integer k: "))
    if k <= 0:
        print("k must be a positive integer.")
        return

    if k > n:
        print("Error: k cannot be greater than N")
        return

    nearest_neighbor = NearestNeighbor(n)
    nearest_neighbor.fit()

    x = float(input("Enter query X: "))
    nearest_neighbor.predict(x, k)

if __name__ == "__main__":
    main()
