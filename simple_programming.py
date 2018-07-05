lines = 0

with open("text/data.dat") as data:
    line = data.readline()

    while line != "":
        num_0 = line.count("0")
        num_1 = line.count("1")

        if num_0 % 3 == 0 or num_1 % 2 == 0:
            lines += 1

        line = data.readline()

print(lines)

############################################################
#                           6662                           #
############################################################