



def draw_rhombus(diameter):
    # print top dot
    print(" " * (diameter - 1) + ".")
    # print top half
    for i in range(1, diameter):
        print(" " * (diameter - i - 1) + "/" + " " * (2 * i - 1) + "\\")
    # print bottom half
    for i in range(diameter - 2, 0, -1):
        print(" " * (diameter - i - 1) + "\\" + " " * (2 * i - 1) + "/")
    # print bottom dot
    print(" " * (diameter - 1) + ".")



draw_rhombus(5)