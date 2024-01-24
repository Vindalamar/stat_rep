import math


def task():
    table = [[0 for _ in range(38)] for _ in range(14)]
    Hab = 0
    Ha = 0
    Hb = 0
    Ha_b = 0
    count = [0 for _ in range(14)]
    for y in range(1, 7):
        for x in range(1, 7):
            table[y + x][x * y] += 1 / 36
            count[y + x] += 1

    for i in range(len(table)):
        if sum(table[i]) != 0:
            Ha -= sum(table[i]) * math.log2(sum(table[i]))
        Hsi = 0
        for x in table[i]:
            if x != 0:
                Hsi -= x / sum(table[i]) * math.log2(x / sum(table[i]))
                Hab -= x * math.log2(x)
        Ha_b += Hsi * count[i] / 36

    for x in range(38):
        summ = 0
        for i in range(len(table)):
            summ += table[i][x]
        if summ != 0:
            Hb -= summ * math.log2(summ)

    res = [round(Hab, 2), round(Ha, 2), round(Hb, 2), round(Ha_b, 2), round(Hb - Ha_b, 2)]
    print(res)


# if __name__ == '__main__':
#     task()
