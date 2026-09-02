#Variables
size = 0
row_num = 0
x = 0

#Main
size = int(input("What size tree you want? "))

for x in range(size):
    row_num = row_num + 1
    print((size - row_num) * " " + (row_num * 2 - 1) * "=")
