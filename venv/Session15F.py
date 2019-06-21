def dataGenerator():
    file = open("students.csv","r")
    lines = file.readlines()

    for line in lines:
        yield line


dg = dataGenerator()
print(next(dg))
print(next(dg))
print(next(dg))


