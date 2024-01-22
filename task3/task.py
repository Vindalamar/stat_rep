import math


def task(csv_str):
    if not csv_str:
        return ""

    n = 5

    res = 0
    for line in csv_str.split('\n'):
        for x in line.split(','):
            if float(x) != 0:
                res += (float(x)/(n-1)) * math.log2(float(x)/(n-1))

    return -res


# if __name__ == '__main__':
#     with open("task3.csv", 'r') as csvf:
#         print(task(csvf.read()))
#     csvf.close()
