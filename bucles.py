for i in range(0, 10):
    for x in range(1, 6):
        rs = ""
        for z in range(0, x):
            rs += "* "
        print(rs)
    for x in range(1, 5):
        rs = ""
        for z in range(0, 5 - x):
            rs += "* "
        print(rs)
