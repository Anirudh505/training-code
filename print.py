for r in range(5):
    for c in range(5):
        if r % 2 == 0:
            if c == 4:
                print(r + 2, end="")
            else:
                print(r + 1, end="")
        else:
            if c == 0:
                print(r + 2, end="")
            else:
                print(r + 1, end="")
    print()