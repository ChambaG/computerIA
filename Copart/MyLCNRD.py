def lcnrd(word):
    file = open('sample.txt', 'r')
    wFile = open('sample2.txt', 'w+')

    line = file.readline()
    keyword = word
    x = 0

    while line != "":
        line = file.readline()
        if keyword in line:
            wFile.write(line)

