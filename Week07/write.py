filename = "count.txt"
def writeNumber (number):
    with open (filename, "wt") as f:
        f.write(str(number))

writeNumber(3)        