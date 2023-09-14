import csv
import argparse

def read_line(path, row_c, col_c):
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile)
        i = 0
        for row in spamreader:
            if i == row_c:
                print(row[col_c])
                break
            i += 1




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('row', type=int)
    parser.add_argument('col', type=int)
    args = parser.parse_args()
    read_line(args.path, args.row, args.col)

