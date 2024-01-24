import numpy as np
import json


def lesserOrEq(x1, x2, js):
    if x1 == x2:
        return True
    for c in js:
        if x1 in c and x2 in c:
            return True
        if x1 in c:
            return True
        if x2 in c:
            return False


def getSub(x1, js):
    for c in js:
        for x in c:
            if x1 == x:
                return c
    return -1



def task(json_f, json_s):
    js_f = json.loads(json_f)
    js_s = json.loads(json_s)

    jsfl = []
    cat1 = []
    jssl = []
    cat2 = []

    for inexplen in js_f:
        if isinstance(inexplen, list):
            jsfl.append(inexplen)
            for x in inexplen:
                cat1.append(x)
        else:
            jsfl.append([inexplen])
            cat1.append(inexplen)

    for inexplen in js_s:
        if isinstance(inexplen, list):
            jssl.append(inexplen)
            for x in inexplen:
                cat2.append(x)
        else:
            jssl.append([inexplen])
            cat2.append(inexplen)

    Yf = [[0 for _ in range(sum(len(c) for c in jsfl))] for _ in range(sum(len(c) for c in jsfl))]
    Ys = [[0 for _ in range(sum(len(c) for c in jssl))] for _ in range(sum(len(c) for c in jssl))]

    for x in range(len(Yf)):
        for y in range(len(Yf)):
            if lesserOrEq(cat1[x], cat1[y], jsfl):
                Yf[x][y] = 1

    for x in range(len(Ys)):
        for y in range(len(Ys)):
            if lesserOrEq(cat2[x], cat2[y], jssl):
                Ys[x][y] = 1

    Yfm = np.array(Yf)
    Ysm = np.array(Ys)

    experts = [Yfm, Ysm]

    explen = len(experts)
    inexplen = len(experts[0])

    ranks = [[0 for _ in range(explen)] for _ in range(inexplen)]
    for x in range(explen):
        for y in range(inexplen):
            ranks[y][x] = len(experts[x][y]) - np.sum(experts[x][y]) + 1

    subd = 0
    for x in range(explen):
        set_n = {}
        for ent in ranks:
            if set_n.get(ent[x]) is None:
                set_n[ent[x]] = 0
            set_n[ent[x]] = set_n[ent[x]] + 1
        for c in set_n:
            subd += set_n[c] ** 3 - set_n[c]
        for y in range(len(ranks)):
            ranks[y][x] = ranks[y][x] + (set_n[ranks[y][x]] - 1) / 2

    mean = np.sum(ranks) / inexplen

    sub2 = 0
    for rank in ranks:
        sub2 += (np.sum(rank) - mean) ** 2

    dmax = (explen * explen * (inexplen ** 3 - inexplen) - explen * subd) / 12

    res = sub2 / dmax
    return round(res, 2)


# if __name__ == "__main__":
#     with open("Ранжировка  A.json", 'r') as csvf:
#         str1 = csvf.read()
#         csvf.close()
#     with open("Ранжировка  B.json", 'r') as csvs:
#         str2 = csvs.read()
#         csvs.close()
#
#     print(task(str1, str2))
