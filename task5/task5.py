import json

def lesser(x1, x2, js):
    if x1 == x2:
        return False
    for c in js:
        if x1 in c and x2 in c:
            return False
        if x1 in c:
            return True
        if x2 in c:
            return False

def Equal(x1, x2, js):
    if x1 == x2:
        return True
    for c in js:
        if x1 in c and x2 in c:
            return True
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

    for n in js_f:
        if isinstance(n, list):
            jsfl.append(n)
            for x in n:
                cat1.append(x)
        else:
            jsfl.append([n])
            cat1.append(n)

    for n in js_s:
        if isinstance(n, list):
            jssl.append(n)
            for x in n:
                cat2.append(x)
        else:
            jssl.append([n])
            cat2.append(n)

    core = []
    cat3 = []
    for x1 in cat1:
        for x2 in cat1:
            if lesser(x1, x2, jsfl) and not lesser(x1, x2, jssl) or (not lesser(x1, x2, jsfl) and lesser(x1, x2, jssl)):
                if Equal(x1, x2, jsfl) or Equal(x1, x2, jssl):
                    continue
                if [x2, x1] not in core:
                    core.append([x1, x2])
                    cat3.append(x1)
                    cat3.append(x2)


    result = []

    for ent in jsfl:
        if len(ent) == 1 and ent[0]:
            if ent[0]not in cat3:
                result.append(ent)
            else:
                result.append(getSub(ent[0], core))

        if len(ent) != 1:
            for x in ent:
                r = []
                if x not in cat3:
                    r.append(x)
                    sub = getSub(x, jssl)
                    for s in sub:
                        if s != x and s in ent and s not in cat3:
                            r.append(s)
                    result.append(r.copy())
                if x in cat3:
                    sub = getSub(x, core)
                    result.append(sub.copy())

    final = []
    cat4 = []
    for ent in result[::-1]:
        if len(ent) == 1:
            final.append(ent[0])
        else:
            if sorted(ent) not in cat4:
                final.append(sorted(ent))
                cat4.append(sorted(ent))
    final = final[::-1]

    return str(final)





# if __name__ == '__main__':
#     with open("Ранжировка  A.json", 'r') as csvf:
#         str1 = csvf.read()
#         csvf.close()
#     with open("Ранжировка  B.json", 'r') as csvs:
#         str2 = csvs.read()
#         csvs.close()
#
#     print(task(str1, str2))
