rows = 5
col = 5
pattern = (
    {3},
    {2,4},
    {1,2,4,5},
    {2,4},
    {3}
)

for i in range(rows):
    for j in range(1, col+1):
        if j in pattern[i]:
            print("*", end="")
        else:
            print(" ", end="")
    print()


