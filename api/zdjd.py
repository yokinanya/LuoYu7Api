import base64

b64 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/="
leftEye = ["o", "0", "O", "Ö"]
mouse = ["w", "v", ".", "_"]
rightEye = ["o", "0", "O", "Ö"]
table = []

separator = " "


def makeTable():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                table.append(leftEye[i] + mouse[j] + rightEye[k])


def human2zdjd(t):
    t = base64.b64encode(t.encode()).decode()
    length = len(t)
    arr = []

    for i in range(length):
        c = t[i]
        n = b64.index(c)
        arr.append(table[n])

    data = separator.join(arr)
    return data


def zdjd2human(t):
    arr = t.split(separator)
    length = len(arr)
    resultArr = []
    for i in range(length):
        c = arr[i]
        if not c:
            continue
        n = table.index(c)
        if n < 0:
            raise ValueError("Invalid zdjd code")
        resultArr.append(b64[n])
    t = "".join(resultArr)
    t = base64.b64decode(t.encode()).decode()
    return t


def isZdjd(t):
    try:
        zdjd2human(t)
        return True
    except:
        return False
