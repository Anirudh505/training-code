def f(n):
    u = str(n)
    v = 0
    for w in range(len(u)):
        v += int(u[w]) ** (w + 1)
    return v == n

print("1. Find first n Disarium numbers")
print("2. Find Disarium numbers between two numbers")

o = int(input("Enter choice (1 or 2): "))

if o == 1:
    p = int(input("Enter how many Disarium numbers to find: "))
    q = 0
    r = 0
    while q < p:
        if f(r):
            print(r, end=" ")
            q += 1
        r += 1

elif o == 2:
    s = int(input("Enter starting number: "))
    t = int(input("Enter ending number: "))
    for u in range(s, t + 1):
        if f(u):
            print(u, end=" ")

else:
    print("Invalid choice!")