import csv


def read_blacklist():
    blacklist = {}
    with open("api/blcaklist.csv", "r", encoding="utf8") as file:
        # 创建CSV读取器
        csv_reader = csv.DictReader(file, fieldnames=["qqid", "reason", "type"])
        next(csv_reader)
        for row in csv_reader:
            blacklist[row["qqid"]] = {}
            blacklist[row["qqid"]]["reason"] = row["reason"]
            blacklist[row["qqid"]]["type"] = row["type"]
    return blacklist


def check_isinblacklist(qqid: int):
    blacklist = read_blacklist()
    try:
        blacklist[qqid]
        reason = blacklist[qqid]["reason"]
        type = blacklist[qqid]["type"]
        status = 200
    except KeyError:
        reason = "404 NOT FOUND"
        type = "#404"
        status = 404
    return status, reason, type
