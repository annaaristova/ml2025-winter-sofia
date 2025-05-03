N = int(input("Enter a positive integer: "))

nums = []
for i in range(N):
    num = int(input("Enter a number: "))
    nums.append(num)
    i += 1

X = int(input("Enter a number to search for: "))

if X in nums :
    index = nums.index(X) + 1
    print(index)
else:
    print(-1)