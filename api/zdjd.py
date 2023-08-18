import base64

b64 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/="

left_eye = ["o", "0", "O", "Ö"]
mouse = ["w", "v", ".", "_"]
right_eye = ["o", "0", "O", "Ö"]
table = []

separator = " "

def make_table():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                table.append(left_eye[i] + mouse[j] + right_eye[k])

make_table()

def add_calls(t):
    return t


def human2zdjd(t):
    t = base64.b64encode(t.encode()).decode()
    length = len(t)
    arr = []

    for i in range(length):
        c = t[i]
        if not c == "=":
            n = b64.index(c)
            arr.append(table[n])

    data = separator.join(arr)
    return add_calls(data)


def zdjd2human(t):
    arr = t.split(separator)
    length = len(arr)
    result_arr = []

    for i in range(length):
        c = arr[i]
        if not c:
            continue
        n = table.index(c)
        if n < 0:
            raise ValueError("Invalid zdjd code")
        result_arr.append(b64[n])

    t = "".join(result_arr)
    padding = length % 4
    if padding > 0:
        t += "=" * (4 - padding)
    t = base64.b64decode(t.encode()).decode()
    return t


def isZdjd(t):
    try:
        zdjd2human(t)
        return True
    except:
        return False
