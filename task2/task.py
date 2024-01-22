# import csv
# import argparse


def task(csv_str):
    if not csv_str:
        return ""

    table = []
    for line in csv_str.split('\n'):
        x, y = line.split(',')
        table.append([int(x),int(y)])

    c = 0
    for duo in table:
        if max(duo) > c:
            c = max(duo)

    res = [[0, 0, 0, 0, 0] for _ in range(c)]

    for duo in table:
        res[duo[0] - 1][0] += 1
        res[duo[1] - 1][1] += 1

    for duo in table[::-1]:
        res[duo[0] - 1][2] += res[duo[1] - 1][0] + res[duo[1] - 1][2]

    for duo in table:
        res[duo[1] - 1][3] += res[duo[0] - 1][3] + res[duo[0] - 1][1]
        res[duo[1] - 1][4] = res[duo[0] - 1][0] - 1

    res_str = ""

    for line in res:
        for num in line[:-1]:
            res_str += str(num) + ','
        res_str += str(line[-1]) + '\n'

    return res_str



# if __name__ == '__main__':
#     task("")
#     # with open("task2.csv", 'r') as csvf:
#     #     print(task(csvf.read()))
#     # csvf.close()
