
def star_pyramid(row_num):
    for i in range(1, row_num + 1):
        # preceding space for each row
        for j in range(row_num - i):
            print(" ", end="")
        # number of stars
        for k in range(i):
            print("*", end=" ")
        print()


star_pyramid(4)

