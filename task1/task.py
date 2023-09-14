import csv


def read_line(path, row_c):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            if i == row_c:
                print(', '.join(row))
            i += 1




if __name__ == '__main__':
    read_line('example.csv', 1)

