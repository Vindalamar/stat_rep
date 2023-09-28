import csv


def read_line(path, row_c, col_c):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in spamreader:
            if i == row_c:
                print(row[col_c])
                break
            i += 1




if __name__ == '__main__':
    read_line('example.csv', 1, 5)

